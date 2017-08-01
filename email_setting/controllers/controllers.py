# -*- coding: utf-8 -*-
from odoo import http

# class EmailSetting(http.Controller):
#     @http.route('/email_setting/email_setting/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/email_setting/email_setting/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('email_setting.listing', {
#             'root': '/email_setting/email_setting',
#             'objects': http.request.env['email_setting.email_setting'].search([]),
#         })

#     @http.route('/email_setting/email_setting/objects/<model("email_setting.email_setting"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('email_setting.object', {
#             'object': obj
#         })