# -*- coding: utf-8 -*-
# from odoo import http


# class InvoiceFinalClient(http.Controller):
#     @http.route('/invoice_final_client/invoice_final_client/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invoice_final_client/invoice_final_client/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('invoice_final_client.listing', {
#             'root': '/invoice_final_client/invoice_final_client',
#             'objects': http.request.env['invoice_final_client.invoice_final_client'].search([]),
#         })

#     @http.route('/invoice_final_client/invoice_final_client/objects/<model("invoice_final_client.invoice_final_client"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invoice_final_client.object', {
#             'object': obj
#         })
