from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    customer_reference_number = fields.Char(string='Customer Reference Number')

    def write(self, vals):
        result = super().write(vals)
        if 'customer_reference_number' in vals and not self.env.context.get('skip_customer_reference_sync'):
            sale_orders = self.filtered(
                lambda move: move.move_type in ('out_invoice', 'out_refund', 'out_receipt')
            ).mapped('invoice_line_ids.sale_line_ids.order_id')
            sale_orders.write({
                'customer_reference_number': vals['customer_reference_number'],
            })
        return result
