# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request
import smtplib


class AuthSignupHomeInherit(AuthSignupHome):

    def do_signup(self, qcontext):
        super(AuthSignupHomeInherit,self).do_signup(qcontext)
        mail_mail_obj = request.env['mail.mail']
        mail_content = (mail_mail_obj.create({
            'email_from': 'Odoo',
            'subject': 'Notification',
            'email_to': qcontext['login'],
            'body_html': 'Sign up successfully! Welcome to Odoo, ' + qcontext['name']
        }))
        mail_content.send()

