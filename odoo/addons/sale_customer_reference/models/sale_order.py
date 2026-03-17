from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    customer_reference_number = fields.Char(string='Customer Reference Number')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('customer_reference_number') and not vals.get('client_order_ref'):
                vals['client_order_ref'] = vals['customer_reference_number']
        orders = super().create(vals_list)
        orders._sync_customer_reference_number()
        return orders

    def _sync_customer_reference_number(self):
        for order in self:
            if order.client_order_ref != order.customer_reference_number:
                order.with_context(skip_customer_reference_sync=True).write({
                    'client_order_ref': order.customer_reference_number,
                })
            if order.picking_ids:
                order.picking_ids.with_context(skip_customer_reference_sync=True).write({
                    'customer_reference_number': order.customer_reference_number,
                })
            draft_invoices = order.invoice_ids.filtered(lambda move: move.state == 'draft')
            if draft_invoices:
                draft_invoices.with_context(skip_customer_reference_sync=True).write({
                    'customer_reference_number': order.customer_reference_number,
                })

    def action_confirm(self):
        result = super().action_confirm()
        self._sync_customer_reference_number()
        return result

    def write(self, vals):
        if 'customer_reference_number' in vals and 'client_order_ref' not in vals:
            vals['client_order_ref'] = vals['customer_reference_number']
        elif 'client_order_ref' in vals and 'customer_reference_number' not in vals:
            vals['customer_reference_number'] = vals['client_order_ref']
        result = super().write(vals)
        if 'customer_reference_number' in vals and not self.env.context.get('skip_customer_reference_sync'):
            self._sync_customer_reference_number()
        return result

    def _prepare_invoice(self):
        values = super()._prepare_invoice()
        values['customer_reference_number'] = self.customer_reference_number
        return values
