-- sql/create_tables_postgres.sql

-- Orders table (raw transactional data)
CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    order_date DATE NOT NULL,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    total_amount FLOAT NOT NULL
);

-- Payments table (linked to orders)
CREATE TABLE IF NOT EXISTS payments (
    payment_id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    payment_method VARCHAR(50),
    payment_status VARCHAR(50),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
