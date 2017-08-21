# -*- coding: utf-8 -*-
from . import test
from odoo import http
from odoo.http import request
import datetime, time

class PlayMusic(http.Controller):
    @http.route('/web/play_music/', auth='public', type="http")
    def index(self, **kw):
        name = request.params.get('name')
        song = request.env['playmusic'].search([('name', '=', name)])
        temp = song.link
        now = time.mktime(datetime.datetime.now().timetuple())
        if request.env['playmusic'].search([('name', '=', name)]).src:
            exp = int(request.env['playmusic'].search([('name', '=', name)]).src.split('exp=')[1].split('~acl')[0])
        if song.src and now <= exp:
            src = song.src
        else:
            src = test.test().get_src(temp)

        request.env['playmusic'].search([('name', '=', name)]).src = src
        vals = {
            'songs': request.env['playmusic'].search([('name', '=', name)])
        }
        return request.render('play_music.play3', vals)

    @http.route('/web/music/', auth='public', type="http")
    def index3(self):
        list = request.env['playmusic'].search([])
        for item in list:
            now = time.mktime(datetime.datetime.now().timetuple())
            if item.src:
                exp = int(item.src.split('exp=')[1].split('~acl')[0])
            if item.src and now <= exp:
                continue
            else:
                item.src = test.test().get_src(item.link)
        vals = {
            'songs': list
        }
        return request.render('play_music.play3', vals)


