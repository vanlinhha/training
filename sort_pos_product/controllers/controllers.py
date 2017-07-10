# -*- coding: utf-8 -*-
from odoo import http

# class SortPosProduct(http.Controller):
#     @http.route('/sort_pos_product/sort_pos_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sort_pos_product/sort_pos_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sort_pos_product.listing', {
#             'root': '/sort_pos_product/sort_pos_product',
#             'objects': http.request.env['sort_pos_product.sort_pos_product'].search([]),
#         })

#     @http.route('/sort_pos_product/sort_pos_product/objects/<model("sort_pos_product.sort_pos_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sort_pos_product.object', {
#             'object': obj
#         })