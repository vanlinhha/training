# -*- coding: utf-8 -*-
from odoo import models, fields, api

class email_setting(models.TransientModel):
    _inherit = "res.config.settings"
    # email_setting = fields.Boolean(string="OES Setting", help="Allow user to set up and change outgoing mail server",default=False)

class email_setting_incoming(models.Model):
    _inherit = "fetchmail.server"