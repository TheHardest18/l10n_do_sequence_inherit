# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InvoiceFinalClient(models.Model):
    _inherit = 'account.move'

    final_customer = fields.Char("Consumidor Final")


class SaleFinalClient(models.Model):
    _inherit = 'sale.order'

    final_customer = fields.Char("Consumidor Final")
