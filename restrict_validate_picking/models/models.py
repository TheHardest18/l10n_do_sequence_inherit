# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class restrict_validate_picking(models.Model):
#     _name = 'restrict_validate_picking.restrict_validate_picking'
#     _description = 'restrict_validate_picking.restrict_validate_picking'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
