# -*- coding: utf-8 -*-
from odoo import http

# class ExportAllPo(http.Controller):
#     @http.route('/export_all_po/export_all_po/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/export_all_po/export_all_po/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('export_all_po.listing', {
#             'root': '/export_all_po/export_all_po',
#             'objects': http.request.env['export_all_po.export_all_po'].search([]),
#         })

#     @http.route('/export_all_po/export_all_po/objects/<model("export_all_po.export_all_po"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('export_all_po.object', {
#             'object': obj
#         })