# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class SaleOrderLine(models.Model):
    _inherit='sale.order.line'
    
    version = fields.Char('Versión')
    observ = fields.Char('Observación')
    base = fields.Float('Base')
    alt = fields.Float('Altura')
    price_m2 = fields.Float('Precio m2')
    price_unit = fields.Float(compute='_compute_price_unit', store=True)
    
    @api.depends('price_m2', 'base', 'alt')
    def _compute_price_unit(self):
        for rec in self:
            if rec.price_m2:
                rec.price_unit = rec.base*rec.alt*rec.price_m2
    
    
class mrp_new_fields(models.Model):
    _inherit = 'mrp.production'
    
    mrp_title = fields.Char(string="Titulo")
    version = fields.Char('Versión')
    observ = fields.Char('Observación')
    observm = fields.Char('Observaciónes Materiales')
    base = fields.Float('Base')
    alt = fields.Float('Altura')
    price_m2 = fields.Float('Precio m2')
    description = fields.Char(string="Descripcion")

class MrpWorkoder(models.Model):
    _inherit = 'mrp.workorder'
    
    version = fields.Char(related="production_id.version", string='Versión')
    observ = fields.Char(related="production_id.observ", string='Observación')
    observm = fields.Char(related="production_id.observm", string='Observaciónes Materiales')
    base = fields.Float(related="production_id.base", string='Base')
    alt = fields.Float(related="production_id.alt", string='Altura')
    price_m2 = fields.Float(related="production_id.price_m2", string='Precio m2')
    
    
class sale_new_fields(models.Model):
    _inherit = 'sale.order'

    sale_title = fields.Char(string="Titulo")
    state = fields.Selection(selection_add=[('no_invoice', 'NO FACTURAR'),('done',)], compute='compute_no_invoice', store=True)
    no_invoice = fields.Boolean(string="No Facturar", compute="compute_no_invoice_bool", store=True)

    @api.depends('state', 'no_invoice')
    def compute_no_invoice_bool(self):
        for rec in self:
            if rec.state not in ['no_invoice', 'sale']:
                self.no_invoice = False
            
                
    @api.depends('state', 'no_invoice')
    def compute_no_invoice(self):
        for rec in self:
            
            if self.no_invoice == True:
                rec.state = 'no_invoice'
    
    def action_confirm(self):
        res = super(sale_new_fields, self).action_confirm()
        active_id =  self.env.context.get('active_ids')
        mrp_active = self.env['mrp.production'].browse(self.env.context.get("active_ids"))
        procurement_groups = self.env['procurement.group'].search([('sale_id', 'in', self.ids)])
        mrp_production_ids = set(procurement_groups.stock_move_ids.created_production_id.procurement_group_id.mrp_production_ids.ids) | set(procurement_groups.mrp_production_ids.ids)
        for rec in self.order_line:
            for line in procurement_groups.stock_move_ids.created_production_id.procurement_group_id.mrp_production_ids:
                if line.product_id.id == rec.product_id.id:
                    line.update({
                        'product_id': rec.product_id.id,
                        'product_qty': rec.product_uom_qty,
                        'product_uom_id': rec.product_id.uom_id.id,
                        'mrp_title': self.sale_title,
                        'version': rec.version,
                        'observ': rec.observ,
                        'base': rec.base,
                        'alt': rec.alt,
                        'price_m2': rec.price_m2,
                        'description': rec.name
                })
        return res

    
