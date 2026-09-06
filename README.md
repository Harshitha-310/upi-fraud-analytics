# UPI Fraud Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458)
![SQL](https://img.shields.io/badge/SQL-Analysis-orange)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)

An end-to-end **UPI fraud analytics project** that generates synthetic transaction data, cleans and scores it, performs exploratory and SQL analysis, detects amount-based anomalies, and presents fraud-risk insights through an interactive **Power BI dashboard**.

> **Portfolio project:** The dataset is synthetic and created for educational/portfolio purposes. It does not contain real UPI, banking, customer, or merchant data.

---

## 📌 What This Project Does

This project demonstrates a complete analytics workflow:

```text
Generate Data
     ↓
Clean & Transform
     ↓
Fraud Risk Signals
     ↓
Anomaly Detection
     ↓
Exploratory Data Analysis
     ↓
SQL Analysis
     ↓
SQLite Database
     ↓
Power BI Data Model
     ↓
Interactive Dashboard
     ↓
Business Insights
```

The default pipeline creates **20,000 synthetic UPI transactions** with transaction, customer, merchant, payment, time, device, beneficiary, amount, and fraud attributes.

---

# 🎯 Business Questions

The project is designed to answer questions such as:

- What is the overall fraud rate?
- How much transaction value is associated with fraud?
- Which payment modes have higher fraud rates?
- Which cities show elevated fraud risk?
- During which hours is fraud more concentrated?
- Which merchant categories have higher fraud rates?
- Are new devices associated with higher fraud risk?
- Are new beneficiaries associated with higher fraud risk?
- Which transactions are unusually high-value?
- Which customers have the highest transaction value?

---

# 🛠️ Technology Stack

| Technology | Usage |
|---|---|
| **Python 3.9+** | Pipeline execution |
| **Pandas** | Data processing |
| **NumPy** | Synthetic data generation |
| **Jupyter Notebook** | Exploratory analysis |
| **SQL** | Analytical queries |
| **SQLite** | Local database |
| **Power BI Desktop** | Interactive dashboard |
| **DAX** | Measures and calculated columns |
| **Power Query (M)** | Data transformation |

---

# 📂 Repository Structure

```text
upi_fraud_analytics/
│
├── data/
│   ├── raw/
│   │   └── upi_transactions.csv
│   └── processed/
│       └── upi_transactions_scored.csv
│
├── dashboard/
│   ├── README / Power BI resources
│   ├── power_query_m.txt
│   └── dax_measures.txt
│
├── notebooks/
│   └── 01_eda_and_anomaly_analysis.ipynb
│
├── reports/
│   └── Business insights and analysis
│
├── sql/
│   ├── 01_schema.sql
│   └── 02_analysis_queries.sql
│
├── src/
│   ├── generate_sample_data.py
│   ├── clean_data.py
│   └── anomaly_detection.py
│
├── tests/
│
├── requirements.txt
├── README.md
└── upi_fraud.db
```

> The exact Power BI `.pbix` filename/location may vary. The repository's dashboard folder contains the supporting Power Query and DAX definitions used to reproduce the model.

---

# 🚀 Quick Start

## Prerequisites

Install:

- **Python 3.9 or newer**
- **Git**
- **Power BI Desktop** — only required for opening/editing the dashboard
- A modern web browser for Jupyter Notebook

Check Python:

```bash
python --version
```

If `python` is unavailable on Windows, try:

```bash
py --version
```

---

## 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd upi_fraud_analytics
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with the URL of your GitHub repository.

Example:

```bash
git clone https://github.com/YOUR_USERNAME/upi-fraud-analytics.git
cd upi-fraud-analytics
```

---

## 2. Create a Virtual Environment

Using a virtual environment is recommended so the project's packages do not interfere with your system Python installation.

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

You should now see `(.venv)` in your terminal.

---

## 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If `pip` is unavailable:

```bash
python -m pip install -r requirements.txt
```

---

# 🔄 Reproduce the Data Pipeline

The project uses three Python scripts instead of a single pipeline script.

Run them in this order.

## Step 1 — Generate Synthetic Data

```bash
python src/generate_sample_data.py
```

Expected output:

```text
Created 20,000 rows at data/raw/upi_transactions.csv
```

This creates:

```text
data/raw/upi_transactions.csv
```

The generated data includes:

- Transaction ID
- Customer ID
- Timestamp
- City
- Payment Mode
- Merchant Category
- Amount
- Hour
- New Device Indicator
- New Beneficiary Indicator
- Fraud Label
- Transaction Status

---

## Step 2 — Clean the Data

```bash
python src/clean_data.py
```

This processes the raw transaction data and prepares it for downstream analysis.

---

## Step 3 — Detect Anomalies / Generate Risk Scores

```bash
python src/anomaly_detection.py
```

This produces the scored dataset used by the analytics workflow.

Expected output:

```text
data/processed/upi_transactions_scored.csv
```

Verify it exists:

### Windows

```bash
dir data\processed
```

### macOS / Linux

```bash
ls data/processed
```

You should see:

```text
upi_transactions_scored.csv
```

---

# 📓 Exploratory Data Analysis

Start Jupyter:

```bash
jupyter notebook
```

Open:

```text
notebooks/01_eda_and_anomaly_analysis.ipynb
```

Then:

1. Select the project's Python kernel.
2. Run the notebook from top to bottom.
3. Use **Kernel → Restart & Run All** if you want to reproduce the complete analysis.

The notebook contains exploratory analysis of:

- Transaction distributions
- Fraud distribution
- Transaction amounts
- Time-based fraud patterns
- City-level fraud
- Merchant-level fraud
- Payment-mode fraud
- Device and beneficiary risk
- Anomaly patterns

---

# 🗄️ SQLite Database

The project uses SQLite for local SQL analysis.

The repository includes:

```text
upi_fraud.db
```

SQLite is accessed through Python's built-in `sqlite3` module, so the project does **not require a separate database server**.

## Recreate the Database

After generating the processed CSV, run:

```bash
python -c "import sqlite3,pandas as pd; df=pd.read_csv('data/processed/upi_transactions_scored.csv'); conn=sqlite3.connect('upi_fraud.db'); df.to_sql('upi_transactions',conn,if_exists='replace',index=False); conn.close(); print(f'Loaded {len(df):,} rows into upi_fraud.db')"
```

Expected output:

```text
Loaded 20,000 rows into upi_fraud.db
```

---

# 🔎 SQL Analysis

The SQL scripts are located in:

```text
sql/
```

### `01_schema.sql`

Defines the transaction table structure.

### `02_analysis_queries.sql`

Contains seven analytical queries:

1. Overall KPI analysis
2. Fraud by payment mode
3. Fraud by city
4. Fraud by hour
5. High-value transactions
6. Customer transaction ranking
7. New device / beneficiary risk

The customer-ranking query demonstrates the use of a SQL window function:

```sql
DENSE_RANK() OVER (ORDER BY total_value DESC)
```

---

# 📊 Power BI Dashboard

The dashboard is organized into three pages.

## Page 1 — Executive Overview

Provides an executive-level summary of fraud activity.

### KPIs

- Total Transactions
- Total Transaction Value
- Fraud Transactions
- Fraud Rate
- Fraud Value

### Visuals

- Total vs. Fraud Value by Month
- Fraud Rate by Merchant Category
- Fraud Rate by City
- Fraud Rate by Payment Mode

---

## Page 2 — Fraud Pattern Analysis

Focuses on identifying where and when fraud risk is concentrated.

### Visuals

- Fraud Rate by Hour
- Fraud Transactions by Day of Week
- Fraud Rate by City
- Fraud Rate by Merchant Category
- Fraud Rate by Payment Mode

### Slicers

- Date
- City
- Payment Mode
- Merchant Category
- Risk Band

---

## Page 3 — Risk & Anomaly Analysis

Provides deeper transaction-level investigation.

### Visuals

- Transaction Amount Distribution
- Amount Anomaly Detection
- Risk Band Distribution
- Fraud Rate by Device Type
- Fraud Rate by Beneficiary Type
- Transaction Details Table

The transaction table includes:

- Transaction ID
- Timestamp
- Amount
- City
- Merchant Category
- Risk Score
- Risk Band
- Status

---

# 📈 Key Results

Using the current generated dataset:

| Metric | Result |
|---|---:|
| Total Transactions | **20,000** |
| Fraud Transactions | **530** |
| Overall Fraud Rate | **2.65%** |
| Total Transaction Value | **~₹28.24M** |
| Fraud Value | **~₹869.8K** |

### Device / Beneficiary Risk

| New Device | New Beneficiary | Transactions | Fraud Transactions | Fraud Rate |
|---:|---:|---:|---:|---:|
| No | Yes | 1,135 | 77 | **6.78%** |
| Yes | Yes | 104 | 6 | **5.77%** |
| Yes | No | 1,544 | 88 | **5.70%** |
| No | No | 17,217 | 359 | **2.09%** |

This indicates that transaction context such as device and beneficiary novelty can be useful as a fraud-risk signal.

---

# 🧠 Anomaly Detection

The project includes amount-based anomaly analysis.

The dashboard compares:

- **IQR-based anomalies**
- **High-value transaction anomalies**

The analysis is intended to identify transactions that differ substantially from normal transaction-value behavior.

---

# 💡 Business Insights

The analysis can help a fraud-monitoring team prioritize transactions involving:

- Higher-risk transaction hours
- New devices
- New beneficiaries
- Large transaction amounts
- Cities with elevated fraud rates
- Merchant categories with elevated fraud rates
- Payment modes with higher fraud rates

The objective is not to label every unusual transaction as fraud, but to provide signals that can help prioritize transactions for investigation.

---

# 🧪 Reproducibility

The project is designed so that another user can reproduce the core analytics workflow from a clean clone.

```text
Clone
  ↓
Create virtual environment
  ↓
Install requirements
  ↓
Generate synthetic data
  ↓
Clean data
  ↓
Run anomaly detection
  ↓
Run Jupyter analysis
  ↓
Create SQLite database
  ↓
Open Power BI dashboard
```

Because the dataset is synthetic and generated with a fixed NumPy random seed, the generated dataset is reproducible when the same code and environment are used.

---

# 🧰 Troubleshooting

## `python` is not recognized

On Windows, try:

```bash
py --version
```

Then use:

```bash
py -m pip install -r requirements.txt
```

and:

```bash
py src/generate_sample_data.py
```

---

## `jupyter` is not recognized

Install Jupyter using:

```bash
python -m pip install notebook
```

Then run:

```bash
jupyter notebook
```

---

## Processed CSV is missing

Run the scripts in this order:

```bash
python src/generate_sample_data.py
python src/clean_data.py
python src/anomaly_detection.py
```

Then check:

```text
data/processed/upi_transactions_scored.csv
```

---

## SQLite CLI is not installed

You do **not** need the `sqlite3` command-line program.

Python includes the `sqlite3` module. Recreate the database using the Python command shown in the **SQLite Database** section.

---

## Power BI cannot find the CSV

The Power BI model may contain a machine-specific file path.

If the CSV path is different on your computer:

1. Open the `.pbix` file in Power BI Desktop.
2. Go to **Transform data**.
3. Open the relevant query in **Power Query**.
4. Update the source path to your local:
   ```text
   data/processed/upi_transactions_scored.csv
   ```
5. Select **Close & Apply**.

The repository includes the Power Query and DAX definitions used by the dashboard to help reproduce the model.

---

# 🔐 Data & Privacy

This project uses **synthetic data only**.

No real:

- Bank account information
- UPI IDs
- Customer personal information
- Financial account records
- Authentication credentials
- Real transaction records

are included.

---

# 🔮 Future Improvements

Possible extensions include:

- Logistic Regression fraud classification
- Random Forest / Gradient Boosting models
- Precision, Recall, and F1-score evaluation
- Class-imbalance handling
- Customer behavioral features
- Real-time fraud scoring
- Automated fraud alerts
- Fraud-risk API
- Time-series fraud forecasting
- Cloud database integration
- Automated Power BI refresh
- Model monitoring and drift detection

---

# 👩‍💻 Skills Demonstrated

### Data Analytics

- Data Cleaning
- Exploratory Data Analysis
- KPI Development
- Fraud Pattern Analysis
- Anomaly Detection
- Business Insight Generation

### Technical

- Python
- Pandas
- NumPy
- SQL
- SQLite
- Power BI
- DAX
- Power Query
- Jupyter Notebook

### Visualization

- KPI Cards
- Line Charts
- Bar Charts
- Donut Charts
- Histograms
- Interactive Slicers
- Transaction Detail Tables

---

# 📜 Disclaimer

This project is created for educational and portfolio purposes using synthetic transaction data. It does not represent real UPI users, banks, merchants, or financial institutions.
