import pandas as pd
import sqlite3
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Paths
DATA_PATH = BASE_DIR / "data" / "employee_sales_raw.csv"
DB_PATH = BASE_DIR / "database" / "company.db"

# Create database folder if not exists
DB_PATH.parent.mkdir(exist_ok=True)

# Connect to database
conn = sqlite3.connect(DB_PATH)

# Read CSV
df = pd.read_csv(DATA_PATH)

# Load into SQL
df.to_sql("employees_raw", conn, if_exists="replace", index=False)

conn.close()

print("✅ Raw data loaded into database successfully")
