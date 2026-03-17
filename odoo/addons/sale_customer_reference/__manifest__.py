# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sale Customer Reference',
    'version': '1.0',
    'category': 'Sales/Sales',
    'summary': 'Track a customer reference number across sales, deliveries, and invoices',
    'depends': ['sale_management', 'sale_stock', 'account'],
    'data': [
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
        'views/account_move_views.xml',
    ],
    'license': 'LGPL-3',
}
