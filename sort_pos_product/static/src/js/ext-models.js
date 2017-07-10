odoo.define('sort_pos_product.models', function (require) {
"use strict";

var BarcodeParser = require('barcodes.BarcodeParser');
var PosDB = require('point_of_sale.DB');
var devices = require('point_of_sale.devices');
var core = require('web.core');
var Model = require('web.DataModel');
var formats = require('web.formats');
var session = require('web.session');
var time = require('web.time');
var utils = require('web.utils');

var QWeb = core.qweb;
var _t = core._t;
var Mutex = utils.Mutex;
var round_di = utils.round_decimals;
var round_pr = utils.round_precision;
var Backbone = window.Backbone;

var exports = {};

exports.PosModel = Backbone.Model.extend({
    initialize: function(session, attributes) {
        Backbone.Model.prototype.initialize.call(this, attributes);
        var  self = this;
        this.flush_mutex = new Mutex();                   // used to make sure the orders are sent to the server once at time
        this.chrome = attributes.chrome;
        this.gui    = attributes.gui;

        this.proxy = new devices.ProxyDevice(this);              // used to communicate to the hardware devices via a local proxy
        this.barcode_reader = new devices.BarcodeReader({'pos': this, proxy:this.proxy});

        this.proxy_queue = new devices.JobQueue();           // used to prevent parallels communications to the proxy
        this.db = new PosDB();                       // a local database used to search trough products and categories & store pending orders
        this.debug = core.debug; //debug mode 
        
        // Business data; loaded from the server at launch
        this.company_logo = null;
        this.company_logo_base64 = '';
        this.currency = null;
        this.shop = null;
        this.company = null;
        this.user = null;
        this.users = [];
        this.partners = [];
        this.cashier = null;
        this.cashregisters = [];
        this.taxes = [];
        this.pos_session = null;
        this.config = null;
        this.units = [];
        this.units_by_id = {};
        this.pricelist = null;
        this.order_sequence = 1;
        window.posmodel = this;

        // these dynamic attributes can be watched for change by other models or widgets
        this.set({
            'synch':            { state:'connected', pending:0 }, 
            'orders':           new OrderCollection(),
            'selectedOrder':    null,
            'selectedClient':   null,
        });

        this.get('orders').bind('remove', function(order,_unused_,options){ 
            self.on_removed_order(order,options.index,options.reason); 
        });

        // Forward the 'client' attribute on the selected order to 'selectedClient'
        function update_client() {
            var order = self.get_order();
            this.set('selectedClient', order ? order.get_client() : null );
        }
        this.get('orders').bind('add remove change', update_client, this);
        this.bind('change:selectedOrder', update_client, this);

        // We fetch the backend data on the server asynchronously. this is done only when the pos user interface is launched,
        // Any change on this data made on the server is thus not reflected on the point of sale until it is relaunched. 
        // when all the data has loaded, we compute some stuff, and declare the Pos ready to be used. 
        this.ready = this.load_server_data().then(function(){
            return self.after_load_server_data();
        });
    },
    after_load_server_data: function(){
         this.load_orders();
         this.set_start_order();
         if(this.config.use_proxy){
             return this.connect_to_proxy();
         }
    },
    // releases ressources holds by the model at the end of life of the posmodel
    destroy: function(){
        // FIXME, should wait for flushing, return a deferred to indicate successfull destruction
        // this.flush();
        this.proxy.close();
        this.barcode_reader.disconnect();
        this.barcode_reader.disconnect_from_proxy();
    },

    connect_to_proxy: function(){
        var self = this;
        var  done = new $.Deferred();
        this.barcode_reader.disconnect_from_proxy();
        this.chrome.loading_message(_t('Connecting to the PosBox'),0);
        this.chrome.loading_skip(function(){
                self.proxy.stop_searching();
            });
        this.proxy.autoconnect({
                force_ip: self.config.proxy_ip || undefined,
                progress: function(prog){ 
                    self.chrome.loading_progress(prog);
                },
            }).then(function(){
                if(self.config.iface_scan_via_proxy){
                    self.barcode_reader.connect_to_proxy();
                }
            }).always(function(){
                done.resolve();
            });
        return done;
    },

    // Server side model loaders. This is the list of the models that need to be loaded from
    // the server. The models are loaded one by one by this list's order. The 'loaded' callback
    // is used to store the data in the appropriate place once it has been loaded. This callback
    // can return a deferred that will pause the loading of the next module. 
    // a shared temporary dictionary is available for loaders to communicate private variables
    // used during loading such as object ids, etc. 
    models: [
    {
        model:  'product.product',
        fields: ['display_name', 'list_price','price','pos_categ_id', 'taxes_id', 'barcode', 'default_code', 
                 'to_weight', 'uom_id', 'description_sale', 'description',
                 'product_tmpl_id','tracking', 'count_sell'],
        order:  ['count_sell desc','sequence','default_code','name'],
        domain: [['sale_ok','=',true],['available_in_pos','=',true]],
        context: function(self){ return { pricelist: self.pricelist.id, display_default_code: false }; },
        loaded: function(self, products){
            self.db.add_products(products);
        },
    },
    ],

    });
return exports;

});
