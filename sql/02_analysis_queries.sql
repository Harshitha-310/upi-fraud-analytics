-- 1. Overall KPI
SELECT
    COUNT(*) AS transactions,
    SUM(amount) AS total_value,
    SUM(is_fraud) AS fraud_transactions,
    ROUND(100.0 * SUM(is_fraud) / COUNT(*), 2) AS fraud_rate_pct,
    SUM(CASE WHEN is_fraud = 1 THEN amount ELSE 0 END) AS fraud_value
FROM upi_transactions;

-- 2. Fraud by payment mode
SELECT
    payment_mode,
    COUNT(*) AS transactions,
    SUM(is_fraud) AS fraud_transactions,
    ROUND(100.0 * SUM(is_fraud) / COUNT(*), 2) AS fraud_rate_pct
FROM upi_transactions
GROUP BY payment_mode
ORDER BY fraud_rate_pct DESC;

-- 3. Fraud by city
SELECT
    city,
    COUNT(*) AS transactions,
    SUM(is_fraud) AS fraud_transactions,
    ROUND(100.0 * SUM(is_fraud) / COUNT(*), 2) AS fraud_rate_pct
FROM upi_transactions
GROUP BY city
ORDER BY fraud_rate_pct DESC;

-- 4. Fraud by hour
SELECT
    hour,
    COUNT(*) AS transactions,
    SUM(is_fraud) AS fraud_transactions,
    ROUND(100.0 * SUM(is_fraud) / COUNT(*), 2) AS fraud_rate_pct
FROM upi_transactions
GROUP BY hour
ORDER BY hour;

-- 5. High-value transactions
SELECT *
FROM upi_transactions
WHERE amount >= 10000
ORDER BY amount DESC;

-- 6. Customer transaction ranking
WITH customer_stats AS (
    SELECT
        customer_id,
        COUNT(*) AS transactions,
        SUM(amount) AS total_value,
        SUM(is_fraud) AS fraud_count
    FROM upi_transactions
    GROUP BY customer_id
)
SELECT *,
       DENSE_RANK() OVER (ORDER BY total_value DESC) AS value_rank
FROM customer_stats;

-- 7. New device / beneficiary risk
SELECT
    is_new_device,
    is_new_beneficiary,
    COUNT(*) AS transactions,
    SUM(is_fraud) AS fraud_transactions,
    ROUND(100.0 * SUM(is_fraud) / COUNT(*), 2) AS fraud_rate_pct
FROM upi_transactions
GROUP BY is_new_device, is_new_beneficiary
ORDER BY fraud_rate_pct DESC;
