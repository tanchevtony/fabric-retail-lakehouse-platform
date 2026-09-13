# Microsoft Fabric Notebooks

## nb_load_bronze

Loads raw CSV files from OneLake into Bronze Delta tables.

Tables Created

- bronze_customers
- bronze_products
- bronze_stores
- bronze_orders
- bronze_order_items
- bronze_returns

---

## nb_silver_transformations

Applies data quality rules and business validations.

Transformations

- Remove null emails
- Remove future dates
- Remove duplicate records
- Validate quantities
- Validate refund amounts

Tables Created

- silver_customers
- silver_products
- silver_stores
- silver_orders
- silver_order_items
- silver_returns

---

## nb_gold_transformations

Creates business-ready analytics datasets.

Tables Created

- gold_customer_lifetime_value
- gold_sales_metrics
- gold_product_performance
- gold_returns_analysis
