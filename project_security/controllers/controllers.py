# -*- coding: utf-8 -*-
from odoo import http

# class ProjectSecurity(http.Controller):
#     @http.route('/project_security/project_security/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_security/project_security/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_security.listing', {
#             'root': '/project_security/project_security',
#             'objects': http.request.env['project_security.project_security'].search([]),
#         })

#     @http.route('/project_security/project_security/objects/<model("project_security.project_security"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_security.object', {
#             'object': obj
#         })