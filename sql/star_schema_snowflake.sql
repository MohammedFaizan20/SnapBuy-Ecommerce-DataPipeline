-- sql/star_schema_snowflake.sql

-- Dimension: Users
CREATE OR REPLACE TABLE dim_user (
    user_id INT PRIMARY KEY,
    user_name STRING,
    email STRING,
    location STRING
);

-- Dimension: Products
CREATE OR REPLACE TABLE dim_product (
    product_id INT PRIMARY KEY,
    product_name STRING,
    category STRING,
    price FLOAT
);

-- Dimension: Dates
CREATE OR REPLACE TABLE dim_date (
    date_id DATE PRIMARY KEY,
    day INT,
    month INT,
    quarter INT,
    year INT
);

-- Fact Table: Orders
CREATE OR REPLACE TABLE fact_orders (
    order_id INT PRIMARY KEY,
    order_date DATE,
    user_id INT,
    product_id INT,
    quantity INT,
    total_amount FLOAT,
    payment_method STRING,
    payment_status STRING,
    FOREIGN KEY (user_id) REFERENCES dim_user(user_id),
    FOREIGN KEY (product_id) REFERENCES dim_product(product_id),
    FOREIGN KEY (order_date) REFERENCES dim_date(date_id)
);
