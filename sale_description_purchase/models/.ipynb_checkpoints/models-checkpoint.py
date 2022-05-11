# -*- coding: utf-8 -*-

from odoo import models, fields, api
from collections import defaultdict
from itertools import groupby
import logging
from datetime import datetime
from dateutil.relativedelta import relativedelta
from itertools import groupby

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.addons.stock.models.stock_rule import ProcurementException

_logger = logging.getLogger(__name__)

class StockRule(models.Model):
    _inherit = 'stock.rule'
    
    @api.model
    def _run_buy(self, procurements):
        res = super(StockRule, self)._run_buy(procurements)
        
        procurements_by_po_domain = defaultdict(list)
        errors = []
        for procurement, rule in procurements:

            # Get the schedule date in order to find a valid seller
            procurement_date_planned = fields.Datetime.from_string(procurement.values['date_planned'])
            schedule_date = (procurement_date_planned - relativedelta(days=procurement.company_id.po_lead))

            supplier = False
            if procurement.values.get('supplierinfo_id'):
                supplier = procurement.values['supplierinfo_id']
            else:
                supplier = procurement.product_id.with_company(procurement.company_id.id)._select_seller(
                    partner_id=procurement.values.get("supplierinfo_name"),
                    quantity=procurement.product_qty,
                    date=schedule_date.date(),
                    uom_id=procurement.product_uom)

            # Fall back on a supplier for which no price may be defined. Not ideal, but better than
            # blocking the user.
            supplier = supplier or procurement.product_id._prepare_sellers(False).filtered(
                lambda s: not s.company_id or s.company_id == procurement.company_id
            )[:1]

            if not supplier:
                msg = _('There is no matching vendor price to generate the purchase order for product %s (no vendor defined, minimum quantity not reached, dates not valid, ...). Go on the product form and complete the list of vendors.') % (procurement.product_id.display_name)
                errors.append((procurement, msg))

            partner = supplier.name
            # we put `supplier_info` in values for extensibility purposes
            procurement.values['supplier'] = supplier
            procurement.values['propagate_cancel'] = rule.propagate_cancel

            domain = rule._make_po_get_domain(procurement.company_id, procurement.values, partner)
            procurements_by_po_domain[domain].append((procurement, rule))

        if errors:
            raise ProcurementException(errors)

        for domain, procurements_rules in procurements_by_po_domain.items():
            # Get the procurements for the current domain.
            # Get the rules for the current domain. Their only use is to create
            # the PO if it does not exist.
            procurements, rules = zip(*procurements_rules)

            # Get the set of procurement origin for the current domain.
            origins = set([p.origin for p in procurements])
            # Check if a PO exists for the current domain.
            po = self.env['purchase.order'].sudo().search([dom for dom in domain], limit=1)
            company_id = procurements[0].company_id
            if not po:
                # We need a rule to generate the PO. However the rule generated
                # the same domain for PO and the _prepare_purchase_order method
                # should only uses the common rules's fields.
                vals = rules[0]._prepare_purchase_order(company_id, origins, [p.values for p in procurements])
                # The company_id is the same for all procurements since
                # _make_po_get_domain add the company in the domain.
                # We use SUPERUSER_ID since we don't want the current user to be follower of the PO.
                # Indeed, the current user may be a user without access to Purchase, or even be a portal user.
                po = self.env['purchase.order'].with_company(company_id).with_user(SUPERUSER_ID).create(vals)
            else:
                # If a purchase order is found, adapt its `origin` field.
                if po.origin:
                    missing_origins = origins - set(po.origin.split(', '))
                    if missing_origins:
                        po.write({'origin': po.origin + ', ' + ', '.join(missing_origins)})
                else:
                    po.write({'origin': ', '.join(origins)})

            procurements_to_merge = self._get_procurements_to_merge(procurements)
            procurements = self._merge_procurements(procurements_to_merge)

            po_lines_by_product = {}
            grouped_po_lines = groupby(po.order_line.filtered(lambda l: not l.display_type and l.product_uom == l.product_id.uom_po_id).sorted(lambda l: l.product_id.id), key=lambda l: l.product_id.id)
            for product, po_lines in grouped_po_lines:
                po_lines_by_product[product] = self.env['purchase.order.line'].concat(*list(po_lines))
            po_line_values = []
            for procurement in procurements:
                po_lines = po_lines_by_product.get(procurement.product_id.id, self.env['purchase.order.line'])
                po_line = po_lines._find_candidate(*procurement)
                
#                 so_lines = procurement[0].group_id.sale_id.order_line
                _logger.error(("LINEASSS esto",procurement.values['group_id'].sale_id.order_line))#.sale_id.order_line))
                _logger.error(("LINEA",po_line.name ))
                so_lines = procurement.values['group_id'].sale_id.order_line
                for line in so_lines:
                    _logger.error((line.product_id.name, po_lines.product_id.name))
                    if line.product_id.id == po_lines.product_id.id:
                        po_lines.name = line.name 

        return res
#          https://github.com/odoo/odoo/blob/a4bc3a5d6fba54bc1b685194c94778ce118d588f/addons/purchase_stock/models/stock_rule.py#L44
#     @api.model
#     def _run_buy(self, procurements):
# #         _logger.error(procurements)
        
#         res = super(StockRule, self)._run_buy(procurements)
#         for procurement in procurements:
#             _logger.error(procurement.values['group_id'].sale_id.order_line)
            
#             so_lines = procurement.values['group_id'].sale_id.order_line
#             for so_line in so_lines:
#                 _logger.error((line.product_id, so_line.product_id))
#                 if line.product_id.id == so_line.product_id.id:
#                     line.name = so_line.name

#         return res