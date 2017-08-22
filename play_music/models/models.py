# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PlayMusic(models.Model):
    _name = "playmusic"
    link = fields.Char(string="Link Zing Mp3 of the song")
    src = fields.Char(string="URL of the song", defeault="")
    name = fields.Char(string="Name", compute="compute_name")

    @api.multi
    def compute_name(self):
        for record in self:
            if record.link:
                record.name = record.link.split("bai-hat/")[1].split("/ZW")[0].replace("-", " ")
            else:
                record.name = " "

    @api.multi
    def play(self):
        return {
            "type": "ir.actions.act_url",
            "url": "/web/play_music/?id=" + str(self.id),
            "target": "self",
        }

    def playall(self):
        return {
            "type" : "ir.actions.act_url",
            "url": "/web/play_all",
            "target": "new"
        }


