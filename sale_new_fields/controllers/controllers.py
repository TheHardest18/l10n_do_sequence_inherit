# -*- coding: utf-8 -*-
# from odoo import http


# class SaleNewFields(http.Controller):
#     @http.route('/sale_new_fields/sale_new_fields/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_new_fields/sale_new_fields/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_new_fields.listing', {
#             'root': '/sale_new_fields/sale_new_fields',
#             'objects': http.request.env['sale_new_fields.sale_new_fields'].search([]),
#         })

#     @http.route('/sale_new_fields/sale_new_fields/objects/<model("sale_new_fields.sale_new_fields"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_new_fields.object', {
#             'object': obj
#         })
