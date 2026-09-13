# Silver Layer Validation

## Results

| Table | Bronze | Silver | Records Removed |
|---------|---------|---------|---------|
| Customers | 100000 | 98000 | 2000 |
| Products | 5000 | 5000 | 0 |
| Stores | 100 | 100 | 0 |
| Orders | 500000 | 499500 | 500 |
| Order Items | 600031 | 600031 | 0 |
| Returns | 25000 | 25000 | 0 |

## Data Quality Rules Applied

### Customers

- Removed null emails
- Removed duplicate customer IDs

### Orders

- Removed future dated orders

### Products

- Validated selling price greater than cost price

### Order Items

- Validated quantity greater than zero

### Returns

- Validated refund amount greater than zero
