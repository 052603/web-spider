# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WebUrl(models.Model):
    _name = 'web.url'
    _rec_name = 'name'

    name = fields.Char(string='站点')
    url = fields.Char(string='URL')
    check = fields.Boolean(string='调度')
    description = fields.Text(string='描述')


    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100