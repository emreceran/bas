# -*- coding: utf-8 -*-
# from odoo import http


# class Bas(http.Controller):
#     @http.route('/bas/bas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bas/bas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bas.listing', {
#             'root': '/bas/bas',
#             'objects': http.request.env['bas.bas'].search([]),
#         })

#     @http.route('/bas/bas/objects/<model("bas.bas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bas.object', {
#             'object': obj
#         })
