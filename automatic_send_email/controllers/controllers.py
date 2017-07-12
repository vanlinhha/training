# -*- coding: utf-8 -*-
from odoo import http

# class AutomaticSendEmail(http.Controller):
#     @http.route('/automatic_send_email/automatic_send_email/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/automatic_send_email/automatic_send_email/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('automatic_send_email.listing', {
#             'root': '/automatic_send_email/automatic_send_email',
#             'objects': http.request.env['automatic_send_email.automatic_send_email'].search([]),
#         })

#     @http.route('/automatic_send_email/automatic_send_email/objects/<model("automatic_send_email.automatic_send_email"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('automatic_send_email.object', {
#             'object': obj
#         })