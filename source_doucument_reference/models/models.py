# -*- coding: utf-8 -*-

from odoo import models, fields, api

class source_doucument_reference(models.Model):
    _inherit = 'account.invoice'

    origin2 = fields.Many2one('sale.order', compute='_origin_compute', string="Source Document", readonly="True")

    @api.depends("origin")
    def _origin_compute(self):
        for item in self:
            order_id = item.origin
            item.origin2 = item.env['sale.order'].search([('name', '=', order_id)])