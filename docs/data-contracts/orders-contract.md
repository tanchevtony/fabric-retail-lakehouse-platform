# Orders Data Contract

## Source System

Sales Platform

## Description

Customer sales transactions.

## Primary Key

order_id

## Refresh Frequency

Daily

## Expected Volume

500,000 records

## Data Quality Rules

- order_id must be unique
- customer_id must exist
- store_id must exist
- total_amount must be positive
- order_date cannot be null

## Owner

Sales Department
