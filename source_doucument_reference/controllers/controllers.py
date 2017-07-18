# -*- coding: utf-8 -*-
from odoo import http

# class SourceDoucumentReference(http.Controller):
#     @http.route('/source_doucument_reference/source_doucument_reference/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/source_doucument_reference/source_doucument_reference/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('source_doucument_reference.listing', {
#             'root': '/source_doucument_reference/source_doucument_reference',
#             'objects': http.request.env['source_doucument_reference.source_doucument_reference'].search([]),
#         })

#     @http.route('/source_doucument_reference/source_doucument_reference/objects/<model("source_doucument_reference.source_doucument_reference"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('source_doucument_reference.object', {
#             'object': obj
#         })