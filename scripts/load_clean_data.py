import pandas as pd
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "database" / "company.db"
DATA_PATH = BASE_DIR / "data" / "employee_sales_clean.csv"

conn = sqlite3.connect(DB_PATH)

df = pd.read_csv(DATA_PATH)
df.to_sql("employees", conn, if_exists="replace", index=False)

conn.close()

print("✅ Clean data loaded into database as 'employees'")
