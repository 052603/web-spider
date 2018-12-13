# -*- coding: utf-8 -*-


from odoo import models, fields, api


class WebUrl(models.Model):
    _name = 'web.url'
    _rec_name = 'name'

    name = fields.Char(string='站点')
    url = fields.Char(string='URL')
    check = fields.Boolean(string='调度')
    description = fields.Text(string='描述')


