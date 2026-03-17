from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_reference_number = fields.Char(string='Customer Reference Number')

    _sql_constraints = [
        (
            'customer_reference_number_unique',
            'unique(customer_reference_number)',
            'Customer Reference Number must be unique.',
        ),
    ]
