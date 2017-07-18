# -*- coding: utf-8 -*-

from odoo import models, fields, api

class auto_create_employee(models.Model):
    _inherit = 'res.users'

    @api.model
    def create(self, vals):
        temp = super(auto_create_employee, self).create(vals)
        self.env['hr.employee'].create(vals)
        return temp


