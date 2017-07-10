odoo.define('sort_pos_product.models', function (require) {
"use strict";

var models = require('point_of_sale.models');
var _super_posmodel = models.PosModel.prototype;

var exports = {};

exports.PosModel = models.Model.extend({
	models: [
	{
        model:  'product.product',
        fields: ['display_name', 'list_price','price','pos_categ_id', 'taxes_id', 'barcode', 'default_code', 
                 'to_weight', 'uom_id', 'description_sale', 'description',
                 'product_tmpl_id','tracking', 'count_sell'],
        order:  ['count_sell','sequence','default_code','name'],
        domain: [['sale_ok','=',true],['available_in_pos','=',true]],
        context: function(self){ return { pricelist: self.pricelist.id, display_default_code: false }; },
        loaded: function(self, products){
            self.db.add_products(products);
        },
    }
	],
});

return exports;
});