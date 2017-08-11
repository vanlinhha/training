# -*- coding: utf-8 -*-

from odoo import models, fields, api

class change_kanban_color(models.Model):
    _inherit = "project.task.type"
    # color = fields.Integer(help="Choose your color", string="Color")
    color = fields.Selection((['0', '0'], ['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7'], ['8', '8'], ['9', '9'] ), string="Select color for your stage", store=True)

#

class change_kanban(models.Model):
    _inherit = "project.task"

    color = fields.Integer(string='Color Index', compute='color_compute', )

    @api.depends("stage_id")
    def color_compute(self):
        for item in self:
            stage_id = item.stage_id.id
            if item.color == 0:
                item.color = item.env['project.task.type'].search([('id', '=',stage_id)]).color
