# -*- coding: utf-8 -*-
from odoo import http

# class OrderLunch(http.Controller):
#     @http.route('/order_lunch/order_lunch/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/order_lunch/order_lunch/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('order_lunch.listing', {
#             'root': '/order_lunch/order_lunch',
#             'objects': http.request.env['order_lunch.order_lunch'].search([]),
#         })

#     @http.route('/order_lunch/order_lunch/objects/<model("order_lunch.order_lunch"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('order_lunch.object', {
#             'object': obj
#         })