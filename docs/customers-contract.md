# Customers Data Contract

## Source System

CRM

## Description

Contains customer demographic and loyalty information.

## Primary Key

customer_id

## Refresh Frequency

Daily

## Expected Volume

100,000 records

## Data Quality Rules

- customer_id must be unique
- email may not be null
- signup_date cannot be future dated

