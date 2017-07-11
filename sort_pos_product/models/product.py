# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from random import randint

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    #count_sell value. Add for sort POS Product by this value.
    count_sell = fields.Integer(string="Count sell item", store=True, compute='_rand_count_count')
    #quantity of product
    quantity = fields.Integer(string="Quantity of product", store=True, compute='_rand_count_quantity')

    #Function to genarate random integer value
    @api.multi
    def _rand_count_count(self):
        for r in self:
            r.count_sell = randint(0, 999)

    @api.multi
    def _rand_count_quantity(self):
        for r in self:
            r.quantity = randint(0, 999)