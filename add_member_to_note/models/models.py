# -*- coding: utf-8 -*-

from odoo import models, fields, api

class add_member_to_note(models.Model):
    _inherit = 'note.note'

    @api.model

    def create(self, vals):
        users = self.env['res.users'].search([]) - self.env.user
        vals['message_follower_ids'] = []
        temp = users.mapped('partner_id')
        for user in temp:
            vals['message_follower_ids'] += self.env['mail.followers']._add_follower_command(self._name, [], {user.id: None}, {}, force=True)[0]
        note = super(add_member_to_note, self).create(vals)
        return note

