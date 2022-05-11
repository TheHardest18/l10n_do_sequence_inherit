# -*- coding: utf-8 -*-
# from odoo import http


# class SaleDescriptionPurchase(http.Controller):
#     @http.route('/sale_description_purchase/sale_description_purchase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_description_purchase/sale_description_purchase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_description_purchase.listing', {
#             'root': '/sale_description_purchase/sale_description_purchase',
#             'objects': http.request.env['sale_description_purchase.sale_description_purchase'].search([]),
#         })

#     @http.route('/sale_description_purchase/sale_description_purchase/objects/<model("sale_description_purchase.sale_description_purchase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_description_purchase.object', {
#             'object': obj
#         })
