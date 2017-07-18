# -*- coding: utf-8 -*-
from odoo import http

# class AutoCreateEmployee(http.Controller):
#     @http.route('/auto_create_employee/auto_create_employee/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/auto_create_employee/auto_create_employee/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('auto_create_employee.listing', {
#             'root': '/auto_create_employee/auto_create_employee',
#             'objects': http.request.env['auto_create_employee.auto_create_employee'].search([]),
#         })

#     @http.route('/auto_create_employee/auto_create_employee/objects/<model("auto_create_employee.auto_create_employee"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('auto_create_employee.object', {
#             'object': obj
#         })