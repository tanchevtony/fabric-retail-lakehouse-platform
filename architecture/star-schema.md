# Retail Warehouse Star Schema

## Overview

The warehouse is designed using a star schema to support analytics and reporting workloads.

## Star Schema

```text
                DimCustomer
                     |
                     |
DimDate ---- FactSales ---- DimProduct
                     |
                     |
                 DimStore
```

## Dimensions

### DimCustomer

Customer attributes:

- customer_id
- first_name
- last_name
- city
- country
- loyalty_tier

### DimProduct

Product attributes:

- product_id
- product_name
- category
- brand

### DimStore

Store attributes:

- store_id
- store_name
- city
- country

### DimDate

Calendar dimension:

- date_key
- date
- year
- month
- month_name
- quarter

## FactSales

Sales transaction metrics:

- order_id
- customer_id
- store_id
- date_key
- total_amount
- sales_channel
```
