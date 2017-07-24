# -*- coding: utf-8 -*-

from odoo import models, fields, api
import smtplib
#
# class automatically_send_email(models.Model):
#     _inherit = 'res.partner'
#


    # @api.model

    # def signup(self, values, token=None):
    #     super(automatically_send_email, self).signup(self, values, token=None)
    #     sender = 'havanlinh1996@gmail.com'
    #     receivers = values['email']
    #
    #     message = 'Sign up successfully!'
    #
    #     smtpObj = smtplib.SMTP(host='smtp.gmail.com', port=587)
    #     smtpObj.ehlo()
    #     smtpObj.starttls()
    #     smtpObj.ehlo()
    #     smtpObj.login(user="havanlinh1996@gmail.com", password="Kaito2011")
    #     smtpObj.sendmail(sender, receivers, message)
    #     print "Successfully sent email"

    # def create(self, cr, uid, vals, context=None):
    #     res = super(automatically_send_email, self).create(cr, uid, vals, context=context)
    #     sender = 'havanlinh1996@gmail.com'
    #     receivers = vals['email']
    #     message = 'Sign up successfully!'
    #     smtpObj = smtplib.SMTP(host='smtp.gmail.com', port=587)
    #     smtpObj.ehlo()
    #     smtpObj.starttls()
    #     smtpObj.ehlo()
    #     smtpObj.login(user="havanlinh1996@gmail.com", password="Kaito2011")
    #     smtpObj.sendmail(sender, receivers, message)
    #     print "Successfully sent email"


