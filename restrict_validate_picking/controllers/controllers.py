# -*- coding: utf-8 -*-
# from odoo import http


# class RestrictValidatePicking(http.Controller):
#     @http.route('/restrict_validate_picking/restrict_validate_picking/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/restrict_validate_picking/restrict_validate_picking/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('restrict_validate_picking.listing', {
#             'root': '/restrict_validate_picking/restrict_validate_picking',
#             'objects': http.request.env['restrict_validate_picking.restrict_validate_picking'].search([]),
#         })

#     @http.route('/restrict_validate_picking/restrict_validate_picking/objects/<model("restrict_validate_picking.restrict_validate_picking"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('restrict_validate_picking.object', {
#             'object': obj
#         })
