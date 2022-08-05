# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class sale_order_multiply(models.Model):
    _name = 'sale_order_multiply.sale_order_multiply'
    _description = 'sale_order_multiply.sale_order_multiply'
    partner_ids = fields.Many2many('res.partner')
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company)
    sale_id = fields.One2many('sale.order.multiply.line','sale_multiply_id')
    sale_orders = fields.One2many('sale.order','sale_id')
    reason_id = fields.Many2one('sale.reason')
    is_other = fields.Boolean()
    reason = fields.Char()


    def get_sale_name(self):
        names = ""
        count = 1
        until = len(self.sale_orders)
        for sale in self.sale_orders:
            if count < until:
                names = names + sale.name + ', '
                count = count + 1
            else:
                names = names + sale.name
        return names


    def action_send_email(self):
        mail_template = self.env.ref('sale_order_multiply.email_template')
        mail_template.send_mail(self.id, force_send=True)

    def get_email_to(self):
        user_group = self.env.ref("sale_order_multiply.group_test_model")
        email_list = [
            usr.partner_id.email for usr in user_group.users if usr.partner_id.email]
        print(email_list)
        return ",".join(email_list)

    def create_sale(self):
        reason = self.reason_id.name
        if self.is_other:
            reason = self.reason

        dict_products = []
        for line in self.sale_id:
            dict_products.append((0, 0, {
                'product_id': line.product_id.id,
                'name': line.description,
                'product_uom_qty': line.quantity,
                'price_unit': line.price,
            }))
        for rec in self.partner_ids:
            self.env['sale.order'].create({
                'partner_id': rec.id,
                'reason': reason,
                'date_order': fields.date.today(),
                'order_line': dict_products,
                'sale_id': self.id,
            })
        self.action_send_email()

class sale_order_lines(models.Model):
    _name = 'sale.order.multiply.line'
    _description = 'product lines'

    product_id = fields.Many2one('product.product')
    description = fields.Char()
    quantity = fields.Float()
    price = fields.Float()
    sale_multiply_id = fields.Many2one('sale_order_multiply.sale_order_multiply')

class sale_order(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(sale_order, self).action_confirm()
        mail_template = self.env.ref('sale_order_multiply.sale_email_template')
        mail_template.send_mail(self.id, force_send=True)
        return res
    def action_cancel(self):
        res = super(sale_order, self).action_cancel()
        mail_template = self.env.ref('sale_order_multiply.sale_email_template1')

        if self.user_id != self.env.user:
            mail_template.send_mail(self.id, force_send=True)
        return res

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    reason = fields.Char()
    sale_id = fields.Many2one('sale_order_multiply.sale_order_multiply')

class SaleReason(models.Model):
    _name = 'sale.reason'
    _description = 'Sale Reason'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)

