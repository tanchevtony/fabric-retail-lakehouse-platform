# Order Items Data Contract

## Description

Contains individual product line items associated with customer orders.

Each record represents one product purchased as part of an order.

## Source System

Sales Platform

## Target Entity

order_items

## Refresh Frequency

Daily

## Primary Key

order_item_id

## Foreign Keys

- order_id references Orders
- product_id references Products

## Expected Volume

Approximately 600,000+ records for the initial dataset.

The number of order items is expected to be greater than the number of orders because a single order can contain multiple products.

## Schema

| Column | Data Type | Description |
|---|---|---|
| order_item_id | string | Unique identifier for an order line item |
| order_id | string | Identifier of the associated order |
| product_id | string | Identifier of the purchased product |
| quantity | integer | Number of units purchased |
| unit_price | decimal | Price per unit at the time of purchase |
| discount_amount | decimal | Discount applied to the order item |

## Data Quality Rules

- order_item_id must not be null.
- order_item_id must be unique.
- order_id must not be null.
- order_id must reference a valid order.
- product_id must not be null.
- product_id must reference a valid product.
- quantity must be greater than zero.
- unit_price must be greater than zero.
- discount_amount must not be negative.
- discount_amount must not exceed the value of the order item.

## Business Rules

An order can contain one or more order items.

Each order item must belong to exactly one order.

Each order item must reference one valid product.

The gross line value can be calculated as:

    quantity × unit_price

The net line value can be calculated as:

    (quantity × unit_price) - discount_amount

## Data Quality Handling

Records that fail Silver-layer validation should not be included in the trusted Silver dataset.

Examples include:

- Invalid product references
- Invalid order references
- Zero or negative quantities
- Invalid prices
- Negative discounts

## Medallion Architecture Mapping

### Bronze

Raw order item records are stored in:

    bronze_order_items

### Silver

Validated order item records are stored in:

    silver_order_items

### Gold

Order item data contributes to business analytics such as:

- Product performance
- Units sold
- Revenue analysis
- Product category performance

## Owner

Sales Department
