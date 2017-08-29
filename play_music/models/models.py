# -*- coding: utf-8 -*-
from odoo import models, fields, api
import requests, json

class PlayMusic(models.Model):
    _name = "playmusic"
    link = fields.Char(string="Zing Mp3, Nhaccuatui link")
    url = fields.Char(string="URL of the song", defeault="")
    # name = fields.Char(string="Name", compute="compute_name")
    title = fields.Char(string="Title", readonly=True)
    artist = fields.Char(string="Artist", readonly=True)
    thumbnail = fields.Char(string="Thumbnail", readonly=True)

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

