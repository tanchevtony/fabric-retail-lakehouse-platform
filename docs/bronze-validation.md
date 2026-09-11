# Bronze Layer Validation

## Summary

All source CSV files were successfully ingested into the Fabric Lakehouse.

| Table | Rows |
|---------|---------|
| bronze_customers | 100000 |
| bronze_products | 5000 |
| bronze_stores | 100 |
| bronze_orders | 500000 |
| bronze_order_items | 600031 |
| bronze_returns | 25000 |

## Validation Checks

- Source files loaded successfully
- Schema inferred successfully
- Delta tables created
- Row counts validated
