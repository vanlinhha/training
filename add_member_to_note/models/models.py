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

class add_member(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals):
        user = super(add_member, self).create(vals)

        for item in self.env['note.note'].search([]):
            self.add_follower_id(item.id, user.id, "note.note")
        return user

    def add_follower_id(self, res_id, partner_id, model):
        followers_obj = self.env['mail.followers']
        reg = {
            'res_id': res_id,
            'res_model': model,
            'partner_id': partner_id, }
        follower_id = followers_obj.create(reg)
        return follower_id

