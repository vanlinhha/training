# -*- coding: utf-8 -*-

from odoo import models, fields, api


#SLACK_TOKEN = 'SLACK_API_HERE'

class OrderLunch(models.Model):
	_name = 'order.lunch'

	@api.model
	def send_notify_slack(self):
		from slacker import Slacker
		slack = Slacker('xoxp-3404732958-164746636839-213505901088-723c7ceb1ec4d2e58923111683253a3b')
		slack.chat.post_message('#lunch_order', 'Sắp đến giờ cơm tối rồi ae ơi!!!', as_user=False)
		print 'haha, cron chạy rội ae ới'
