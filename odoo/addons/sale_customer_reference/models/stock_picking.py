from odoo import fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    customer_reference_number = fields.Char(string='Customer Reference Number')

    def write(self, vals):
        result = super().write(vals)
        if 'customer_reference_number' in vals and not self.env.context.get('skip_customer_reference_sync'):
            for picking in self.filtered('sale_id'):
                picking.sale_id.write({
                    'customer_reference_number': picking.customer_reference_number,
                })
        return result
