from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    customer_reference_number = fields.Char(
        string='Customer Reference Number',
        related='partner_id.customer_reference_number',
        store=True,
        readonly=True,
    )
