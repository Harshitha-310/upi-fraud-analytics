import pandas as pd

INPUT = "data/raw/upi_transactions.csv"
OUTPUT = "data/processed/upi_transactions_clean.csv"

df = pd.read_csv(INPUT, parse_dates=["timestamp"])

df = df.drop_duplicates(subset=["transaction_id"]).copy()
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
df = df[df["amount"] > 0].copy()

df["date"] = df["timestamp"].dt.date
df["month"] = df["timestamp"].dt.to_period("M").astype(str)
df["day_of_week"] = df["timestamp"].dt.day_name()
df["hour"] = df["timestamp"].dt.hour
df["risk_flag"] = (
    (df["amount"] >= df["amount"].quantile(0.99))
    | (df["hour"].between(0, 5))
    | (df["is_new_device"] == 1)
    | (df["is_new_beneficiary"] == 1)
)

df.to_csv(OUTPUT, index=False)
print(f"Saved {len(df):,} cleaned rows to {OUTPUT}")
