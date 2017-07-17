odoo.define('sort_pos_product.models', function(require) {
"use strict";

var models = require('point_of_sale.models');

models.load_models({
	    model:  'product.product',
        fields: ['display_name', 'list_price','price','pos_categ_id', 'taxes_id', 'barcode', 'default_code', 
                 'to_weight', 'uom_id', 'description_sale', 'description',
                 'product_tmpl_id','tracking', 'count_sell', 'quantity', 'qty_available', 'purchase_order_count'],
        order:  [ 'sequence','default_code','name'],
        domain: [['sale_ok','=',true],['available_in_pos','=',true]],
        context: function(self){ return { pricelist: self.pricelist.id, display_default_code: false }; },
        loaded: function(self, products){
        	products.sort(function (a,b) {
        		return (a.purchase_order_count > b.purchase_order_count) ? -1 : ((b.purchase_order_count > a.purchase_order_count) ? 1 : 0);
        	});
        	console.log(products);
            self.db.add_products(products);

        },
});
});