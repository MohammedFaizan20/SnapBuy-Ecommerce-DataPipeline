-- sql/sample_data.sql

-- Users
INSERT INTO dim_user (user_id, user_name, email, location) VALUES
(1, 'Alice Johnson', 'alice@example.com', 'Bangalore'),
(2, 'Bob Smith', 'bob@example.com', 'Mumbai'),
(3, 'Charlie Brown', 'charlie@example.com', 'Delhi');

-- Products
INSERT INTO dim_product (product_id, product_name, category, price) VALUES
(101, 'Wireless Mouse', 'Electronics', 599.00),
(102, 'Bluetooth Speaker', 'Electronics', 1299.00),
(103, 'Notebook', 'Stationery', 49.00);

-- Dates
INSERT INTO dim_date (date_id, day, month, quarter, year) VALUES
('2024-05-01', 1, 5, 2, 2024),
('2024-05-02', 2, 5, 2, 2024),
('2024-05-03', 3, 5, 2, 2024);

-- Orders
INSERT INTO fact_orders (
    order_id, order_date, user_id, product_id, quantity, total_amount, payment_method, payment_status
) VALUES
(1001, '2024-05-01', 1, 101, 1, 599.00, 'UPI', 'completed'),
(1002, '2024-05-02', 2, 102, 2, 2598.00, 'Card', 'completed'),
(1003, '2024-05-03', 3, 103, 3, 147.00, 'Netbanking', 'pending');
