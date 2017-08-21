# -*- coding: utf-8 -*-
from odoo import models, fields, api
import datetime

import threading


class PlayMusic(models.Model):
    _name = "playmusic"
    link = fields.Char(string="Link of the song")
    name = fields.Char(string="Name")
    src = fields.Char(string="URL of the song")
    date = fields.Date(default=datetime.datetime.now().date())

    # @api.model
    # def create(self, vals):
    #     song = super(PlayMusic, self).create(vals)
    #     lock = threading.Lock()
    #     lock.acquire()
    #     song.src = test.test().get_src(song.link)
    #     lock.release()

    # @api.onchange('link')
    # def onchange_link(self):
    #     print self.link
    #     self.src = test.test().get_src(self.link)
    #     print self.link


    @api.multi
    def play(self):
        return {
            "type": "ir.actions.act_url",
            "url": "/web/play_music/?name=" + self.name,
            "target": "new",
        }

    def playall(self):
        print "aaaâ"
        return {
            "type" : "ir.actions.act_url",
            "url": "/web/play_all",
            "target": "new"
        }


