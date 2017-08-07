# -*- coding: utf-8 -*-

from odoo import models, fields, api

class project_security(models.Model):
    # _name = "project_security"

    _inherit = 'project.project'
    # @api.model
    # def del_project_user(self):
    #     self.env["res.groups"].search([('name', '=', 'User')]).unlink()
    #     self.env["res.groups"].search([('name', '=', 'Manager')]).unlink()



