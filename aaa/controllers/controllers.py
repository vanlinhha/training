# -*- coding: utf-8 -*-
from odoo import http

# class Aaa(http.Controller):
#     @http.route('/aaa/aaa/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aaa/aaa/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aaa.listing', {
#             'root': '/aaa/aaa',
#             'objects': http.request.env['aaa.aaa'].search([]),
#         })

#     @http.route('/aaa/aaa/objects/<model("aaa.aaa"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aaa.object', {
#             'object': obj
#         })