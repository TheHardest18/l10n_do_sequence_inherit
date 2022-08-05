# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderMultiply(http.Controller):
#     @http.route('/sale_order_multiply/sale_order_multiply/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_multiply/sale_order_multiply/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_multiply.listing', {
#             'root': '/sale_order_multiply/sale_order_multiply',
#             'objects': http.request.env['sale_order_multiply.sale_order_multiply'].search([]),
#         })

#     @http.route('/sale_order_multiply/sale_order_multiply/objects/<model("sale_order_multiply.sale_order_multiply"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_multiply.object', {
#             'object': obj
#         })
