# Sale Customer Reference

## Task

As part of the onboarding technical task, this customization extends the Odoo sales flow to track a custom field named `Customer Reference Number` across Sales Orders, Delivery Orders, and Customer Invoices.

## Objective

Understand how to:

- extend existing Odoo models
- add custom fields to standard Odoo views
- propagate data across related business documents

## Task Description

The company wants to track an additional reference called `Customer Reference Number` throughout the sales workflow.

This module adds the same field to:

- Sales Order
- Delivery Order
- Customer Invoice

The value entered on the Sales Order is automatically passed to the related Delivery Order and Customer Invoice.

## Requirements

### 1. Sales Order

- Add a field called `Customer Reference Number`
- Model: `sale.order`
- Field type: `fields.Char`
- Display the field in the `Other Information` tab

### 2. Delivery Order

- Add the same field `Customer Reference Number`
- Model: `stock.picking`
- Field type: `fields.Char`

### 3. Customer Invoice

- Add the same field `Customer Reference Number`
- Model: `account.move`
- Field type: `fields.Char`

### 4. Field Behavior

- The value entered on the Sales Order should automatically propagate to:
  - related Delivery Orders
  - related Customer Invoices

## Implementation Summary

### Python Models

The field is added to these models:

- `sale.order`
- `stock.picking`
- `account.move`

Propagation logic is implemented in `sale.order`:

- on Sales Order confirmation, the value is written to related pickings
- when the Sales Order is updated, the value is synced to related pickings and draft invoices
- when invoices are created from the Sales Order, the field is included in invoice values

### XML Views

The field is added to these views:

- Sales Order form
- Delivery Order form
- Customer Invoice form

## Relevant Files

### Python

- [models/sale_order.py](/home/aashriya/Documents/odoo-demo/odoo/addons/sale_customer_reference/models/sale_order.py)
- [models/stock_picking.py](/home/aashriya/Documents/odoo-demo/odoo/addons/sale_customer_reference/models/stock_picking.py)
- [models/account_move.py](/home/aashriya/Documents/odoo-demo/odoo/addons/sale_customer_reference/models/account_move.py)

### XML

- [views/sale_order_views.xml](/home/aashriya/Documents/odoo-demo/odoo/addons/sale_customer_reference/views/sale_order_views.xml)
- [views/stock_picking_views.xml](/home/aashriya/Documents/odoo-demo/odoo/addons/sale_customer_reference/views/stock_picking_views.xml)
- [views/account_move_views.xml](/home/aashriya/Documents/odoo-demo/odoo/addons/sale_customer_reference/views/account_move_views.xml)

### Tests

- [tests/test_customer_reference.py](/home/aashriya/Documents/odoo-demo/odoo/addons/sale_customer_reference/tests/test_customer_reference.py)

## Installation and Update Notes

For a new addon, placing the code in the `addons` path is not enough. The module must also be installed in the target database.

- First-time installation:

```bash
odoo/.venv/bin/python odoo/odoo-bin -c odoo/debian/odoo.conf -d odoo_demo --db_host=127.0.0.1 --db_port=5432 --db_user=odoo --db_password=odoo -i sale_customer_reference --stop-after-init
```

- After making changes to an already installed addon:

```bash
odoo/.venv/bin/python odoo/odoo-bin -c odoo/debian/odoo.conf -d odoo_demo --db_host=127.0.0.1 --db_port=5432 --db_user=odoo --db_password=odoo -u sale_customer_reference --stop-after-init
```

## Deliverables

This task should include:

- Python code for the added fields
- XML code showing where the fields were added in the views
- screenshots showing the field in:
  - Sales Order
  - Delivery Order
  - Customer Invoice

## Suggested Screenshot Checklist

Capture screenshots for:

1. Sales Order showing `Customer Reference Number` in `Other Information`
2. Delivery Order showing the propagated `Customer Reference Number`
3. Customer Invoice showing the propagated `Customer Reference Number`

## Outcome

This task demonstrates how to extend standard Odoo models, modify inherited views, and preserve business data across related documents in the sales workflow.
