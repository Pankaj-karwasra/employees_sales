import pandas as pd
import sqlite3
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Paths
DB_PATH = BASE_DIR / "database" / "company.db"

# Connect to database
conn = sqlite3.connect(DB_PATH)


queries = {
    "avg_salary_by_dept": """
        SELECT department, ROUND(AVG(salary),2) avg_salary
        FROM employees
        GROUP BY department
    """,
    "top_sales_employee": """
        SELECT name, department, monthly_sales
        FROM employees
        ORDER BY monthly_sales DESC
        LIMIT 1
    """,
    "experienced_employees": """
        SELECT name, department, experience
        FROM employees
        WHERE experience >= 5
    """
}

for title, query in queries.items():
    print(f"\n--- {title.upper()} ---")
    print(pd.read_sql(query, conn))

conn.close()