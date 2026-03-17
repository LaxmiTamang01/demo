from odoo.fields import Command
from odoo.tests import tagged

from odoo.addons.sale.tests.common import TestSaleCommon


@tagged('-at_install', 'post_install')
class TestCustomerReference(TestSaleCommon):

    def test_customer_reference_propagation(self):
        sale_order = self.env['sale.order'].create({
            'partner_id': self.partner.id,
            'partner_invoice_id': self.partner.id,
            'partner_shipping_id': self.partner.id,
            'customer_reference_number': 'CRN-001',
            'order_line': [
                Command.create({
                    'product_id': self.product.id,
                    'product_uom_qty': 2.0,
                }),
            ],
        })

        sale_order.action_confirm()

        self.assertTrue(sale_order.picking_ids, 'A delivery order should be generated from the sale order.')
        self.assertEqual(
            sale_order.picking_ids[:1].customer_reference_number,
            'CRN-001',
            'The delivery order should show the sales order customer reference number.',
        )

        invoice = sale_order._create_invoices()

        self.assertEqual(
            invoice.customer_reference_number,
            'CRN-001',
            'The invoice should inherit the sales order customer reference number.',
        )

        sale_order.customer_reference_number = 'CRN-002'

        self.assertEqual(
            sale_order.picking_ids[:1].customer_reference_number,
            'CRN-002',
            'The delivery order should stay in sync with the sales order customer reference number.',
        )
        self.assertEqual(
            invoice.customer_reference_number,
            'CRN-002',
            'Draft invoices should stay in sync with the sales order customer reference number.',
        )
