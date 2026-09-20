-- create DimCustomer
CREATE TABLE dbo.DimCustomer
(
    customer_id VARCHAR(50),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    city VARCHAR(100),
    country VARCHAR(100),
    loyalty_tier VARCHAR(50)
);

-- create DimProduct
CREATE TABLE dbo.DimProduct
(
    product_id VARCHAR(50),
    product_name VARCHAR(255),
    category VARCHAR(100),
    brand VARCHAR(100)
);

-- create DimStore
CREATE TABLE dbo.DimStore
(
    store_id VARCHAR(50),
    store_name VARCHAR(255),
    city VARCHAR(100),
    country VARCHAR(100)
);


-- create DimDate
CREATE TABLE dbo.DimDate
(
    date_key INT,
    date_value DATE,
    year INT,
    month INT,
    month_name VARCHAR(20),
    quarter_number INT
);

-- create FactSales
CREATE TABLE dbo.FactSales
(
    order_id VARCHAR(50),
    customer_id VARCHAR(50),
    store_id VARCHAR(50),
    date_key INT,
    total_amount DECIMAL(18,2),
    sales_channel VARCHAR(50)
);



