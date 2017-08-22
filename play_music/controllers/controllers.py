# -*- coding: utf-8 -*-
from . import test
from odoo import http
from odoo.http import request
import datetime, time

class PlayMusic(http.Controller):
    @http.route('/web/play_music/', auth='public', type="http")
    def index(self, **kw):
        song_id = request.params.get('id')
        song = request.env['playmusic'].search([('id', '=', song_id)])
        temp = song.link
        now = time.mktime(datetime.datetime.now().timetuple())
        if request.env['playmusic'].search([('id', '=', song_id)]).src:
            exp = int(request.env['playmusic'].search([('id', '=', song_id)]).src.split('exp=')[1].split('~acl')[0])
        if song.src and now <= exp:
            src = song.src
        else:
            src = test.test().get_src(temp)

        request.env['playmusic'].search([('id', '=', song_id)]).src = src
        list = request.env['playmusic'].search([]) - request.env['playmusic'].search([('id', '=', song_id)])
        list_data = request.env['playmusic'].search([('id', '=', song_id)]) + list
        vals = {
            'songs': list_data
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


