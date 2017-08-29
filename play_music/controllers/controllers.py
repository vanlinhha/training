# -*- coding: utf-8 -*-
from . import test
from odoo import http
from odoo.http import request
import datetime, time
import requests,json

class PlayMusic(http.Controller):
    @http.route('/web/play_music/', auth='public', type="http")
    def index(self, **kw):
        song_id = request.params.get('id')
        song = request.env['playmusic'].search([('id', '=', song_id)])
        temp = song.link
        now = time.mktime(datetime.datetime.now().timetuple())
        if request.env['playmusic'].search([('id', '=', song_id)]).url:
            exp = int(request.env['playmusic'].search([('id', '=', song_id)]).url.split('exp=')[1].split('~acl')[0])
        if song.url and now <= exp:
            url = song.url
        else:
            url = test.test().get_url(temp)

        request.env['playmusic'].search([('id', '=', song_id)]).url = url
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
            if "nhaccuatui" in item.link:
                if item.url and item.title:
                    if item.thumbnail and item.artist:
                        continue
                else:
                    r = requests.get(
                        "https://mp3zing.download/api?key=QFopqEX1hjMN&url=" + item.link)
                    data = json.loads(r.content)
                    item.title = data["title"]
                    item.url = data["link128"]
                    item.artist = data["artist"]
                    item.thumbnail = data["thumbnail"]
            if "zing" in item.link:
                r = requests.get(
                    "https://mp3zing.download/api?key=QFopqEX1hjMN&url=" + item.link)
                data = json.loads(r.content)
                item.title = data["title"]
                item.url = data["link128"]
                item.artist = data["artist"]
                item.thumbnail = data["thumbnail"]


        # for item in list:
        #     now = time.mktime(datetime.datetime.now().timetuple())
        #     if item.url:
        #         exp = int(item.url.split('exp=')[1].split('~acl')[0])
        #     if item.url and now <= exp:
        #         continue
        #     else:
        #         item.url = test.test().get_url(item.link)

        vals = {
            'songs': list
        }
        return request.render('play_music.play', vals)

    @http.route('/web/music/320', auth='public', type="http")
    def index4(self):
        list = request.env['playmusic'].search([])
        for item in list:
            if "nhaccuatui" in item.link:
                if item.url and item.title:
                    if item.thumbnail and item.artist:
                        continue
                else:
                    r = requests.get(
                        "https://mp3zing.download/api?key=QFopqEX1hjMN&url=" + item.link)
                    data = json.loads(r.content)
                    item.title = data["title"]
                    item.url = data["link320"]
                    item.artist = data["artist"]
                    item.thumbnail = data["thumbnail"]
            if "zing" in item.link:
                r = requests.get(
                    "https://mp3zing.download/api?key=QFopqEX1hjMN&url=" + item.link)
                data = json.loads(r.content)
                item.title = data["title"]
                item.url = data["link320"]
                item.artist = data["artist"]
                item.thumbnail = data["thumbnail"]

        vals = {
            'songs': list
        }
        return request.render('play_music.play', vals)

    @http.route('/web/music/lossless', auth='public', type="http")
    def index5(self):
        list = request.env['playmusic'].search([])
        for item in list:
            if "nhaccuatui" in item.link:
                if item.url and item.title:
                    if item.thumbnail and item.artist:
                        continue
                else:
                    r = requests.get(
                        "https://mp3zing.download/api?key=QFopqEX1hjMN&url=" + item.link)
                    data = json.loads(r.content)
                    item.title = data["title"]
                    item.url = data["lossless"]
                    item.artist = data["artist"]
                    item.thumbnail = data["thumbnail"]
            if "zing" in item.link:
                r = requests.get(
                    "https://mp3zing.download/api?key=QFopqEX1hjMN&url=" + item.link)
                data = json.loads(r.content)
                item.title = data["title"]
                item.url = data["lossless"]
                item.artist = data["artist"]
                item.thumbnail = data["thumbnail"]

        vals = {
            'songs': list
        }
        return request.render('play_music.play', vals)




