-- PostgreSQL-style schema
CREATE TABLE upi_transactions (
    transaction_id VARCHAR(20) PRIMARY KEY,
    customer_id VARCHAR(20),
    timestamp TIMESTAMP,
    city VARCHAR(50),
    payment_mode VARCHAR(30),
    merchant_category VARCHAR(50),
    amount DECIMAL(14,2),
    hour INT,
    is_new_device INT,
    is_new_beneficiary INT,
    is_fraud INT,
    status VARCHAR(20)
);
