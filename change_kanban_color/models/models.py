# -*- coding: utf-8 -*-

from odoo import models, fields, api

class change_kanban_color(models.Model):
    _inherit = "project.task.type"
    color = fields.Integer(help="Choose your color", string="Color")

class change_kanban(models.Model):
    _inherit = "project.task"

    color = fields.Integer(string='Color Index', compute='color_compute', )

    @api.depends("stage_id")
    def color_compute(self):
        for item in self:
            stage_id = item.stage_id.id
            if item.color == 0:
                item.color = item.env['project.task.type'].search([('id', '=',stage_id)]).color
