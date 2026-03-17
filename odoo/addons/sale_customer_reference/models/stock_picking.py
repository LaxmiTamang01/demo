from odoo import fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    customer_reference_number = fields.Char(
        string='Customer Reference Number',
        related='partner_id.customer_reference_number',
        store=True,
        readonly=True,
    )
