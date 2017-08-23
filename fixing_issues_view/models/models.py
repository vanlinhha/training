# -*- coding: utf-8 -*-

from odoo import models, fields, api

class fixing_issues_view(models.Model):
    _inherit = 'project.issue'

    @api.model
    def check_manager(self):
        user = self.env['res.users'].browse(self.env.uid)
        if user.has_group("project.group_project_manager") and user.has_group("project.group_project_user"):
            group_manager = self.env.ref('project.group_project_user')
            group_manager.write({'users': [(3, user.id)]})

