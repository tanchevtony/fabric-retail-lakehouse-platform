# Architecture Decisions

## Decision 1

Use Medallion Architecture.

### Reason

Provides separation between:

- Raw Data
- Clean Data
- Business Data

### Benefits

- Easier debugging
- Better governance
- Reusable datasets
