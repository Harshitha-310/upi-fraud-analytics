import numpy as np
import pandas as pd

RNG = np.random.default_rng(42)

N = 20000
cities = ["Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Chennai",
          "Pune", "Kolkata", "Ahmedabad", "Jaipur", "Lucknow"]
payment_modes = ["UPI", "UPI QR", "UPI Collect", "UPI Intent"]
merchants = ["Retail", "Grocery", "Food", "Travel", "Utilities", "E-commerce"]

dates = pd.date_range("2025-01-01", "2025-12-31", freq="min")
df = pd.DataFrame({
    "transaction_id": [f"TXN{i:07d}" for i in range(1, N + 1)],
    "customer_id": [f"C{i:06d}" for i in RNG.integers(1, 5001, N)],
    "timestamp": RNG.choice(dates, N),
    "city": RNG.choice(cities, N),
    "payment_mode": RNG.choice(payment_modes, N),
    "merchant_category": RNG.choice(merchants, N),
    "amount": np.round(np.exp(RNG.normal(np.log(850), 1.0, N)), 2),
})

df["hour"] = df["timestamp"].dt.hour
df["is_new_device"] = RNG.binomial(1, 0.08, N)
df["is_new_beneficiary"] = RNG.binomial(1, 0.06, N)

# Synthetic fraud label with intentionally explainable risk signals.
risk = (
    0.015
    + 0.025 * (df["amount"] > 10000)
    + 0.025 * (df["hour"].between(0, 5))
    + 0.035 * df["is_new_device"]
    + 0.04 * df["is_new_beneficiary"]
)
risk = np.clip(risk, 0, 0.35)
df["is_fraud"] = RNG.binomial(1, risk)

df["status"] = np.where(df["is_fraud"].eq(1), "Fraud", "Legitimate")
df.to_csv("data/raw/upi_transactions.csv", index=False)
print(f"Created {len(df):,} rows at data/raw/upi_transactions.csv")
