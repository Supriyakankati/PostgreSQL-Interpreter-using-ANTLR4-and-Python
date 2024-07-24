-- Create a simple table with primary key and NOT NULL constraint
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email TEXT UNIQUE
);

-- Create a table with a composite primary key
CREATE TABLE orders (
    order_id SERIAL,
    product_id INT,
    order_date TIMESTAMP,
    PRIMARY KEY (order_id, product_id)
);

-- Create a table with a unique constraint
CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(255) UNIQUE
);

-- Create a table with a boolean column
CREATE TABLE messages (
    message_id SERIAL PRIMARY KEY,
    message_text TEXT,
    is_read BOOLEAN
);

-- Create a table with a composite unique constraint
CREATE TABLE addresses (
    address_id SERIAL PRIMARY KEY,
    street_address VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(2),
    postal_code VARCHAR(10),
    UNIQUE (street_address, city, state, postal_code)
);
