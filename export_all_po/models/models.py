# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ExportPO(models.TransientModel):
    _inherit = 'base.language.export'

    export_all = fields.Boolean('Export all modules', default=False)

    @api.onchange('export_all')
    def _onchange_export_all(self):
        if self.export_all:
            self.modules = self.env['ir.module.module'].search([('state', '=', 'installed')]).ids
        else:
            self.modules = None
