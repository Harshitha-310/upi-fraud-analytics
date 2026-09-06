import pandas as pd
import numpy as np

INPUT = "data/processed/upi_transactions_clean.csv"
OUTPUT = "data/processed/upi_transactions_scored.csv"

df = pd.read_csv(INPUT, parse_dates=["timestamp"])

q1 = df["amount"].quantile(0.25)
q3 = df["amount"].quantile(0.75)
iqr = q3 - q1
upper = q3 + 1.5 * iqr

df["amount_iqr_anomaly"] = (df["amount"] > upper).astype(int)

mean = df["amount"].mean()
std = df["amount"].std(ddof=0)
df["amount_zscore"] = np.where(std == 0, 0, (df["amount"] - mean) / std)
df["high_amount_anomaly"] = (df["amount_zscore"].abs() >= 3).astype(int)

df["risk_score"] = (
    35 * df["amount_iqr_anomaly"]
    + 25 * (df["hour"].between(0, 5).astype(int))
    + 20 * df["is_new_device"]
    + 20 * df["is_new_beneficiary"]
)
df["risk_band"] = pd.cut(
    df["risk_score"],
    bins=[-1, 19, 49, 100],
    labels=["Low", "Medium", "High"]
)

df.to_csv(OUTPUT, index=False)
print(f"Saved scored data to {OUTPUT}")
