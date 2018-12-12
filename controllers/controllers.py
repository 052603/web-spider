# -*- coding: utf-8 -*-
from odoo import http

# class Web-spider(http.Controller):
#     @http.route('/web-spider/web-spider/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/web-spider/web-spider/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('web-spider.listing', {
#             'root': '/web-spider/web-spider',
#             'objects': http.request.env['web-spider.web-spider'].search([]),
#         })

#     @http.route('/web-spider/web-spider/objects/<model("web-spider.web-spider"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('web-spider.object', {
#             'object': obj
#         })