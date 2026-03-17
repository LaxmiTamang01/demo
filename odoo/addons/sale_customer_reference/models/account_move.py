from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    customer_reference_number = fields.Char(
        string='Customer Reference Number',
        related='partner_id.customer_reference_number',
        store=True,
        readonly=True,
    )
