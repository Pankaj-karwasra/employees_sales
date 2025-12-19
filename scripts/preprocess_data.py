import pandas as pd
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Paths
DATA_PATH = BASE_DIR / "data" / "employee_sales_raw.csv"

df = pd.read_csv(DATA_PATH)

df = df.drop_duplicates()

df['salary'] = df.groupby('department')['salary'].transform(
    lambda x:x.fillna(x.mean())
)

df['monthly_sales'].fillna(df['monthly_sales'].mean(),inplace=True)


df['experience'].fillna(df['experience'].median(),inplace=True)

df['city'].fillna(df['city'].mode()[0],inplace=True)

df['join_date'].fillna(method='ffill',inplace=True)

df['join_date'] = pd.to_datetime(df['join_date'])

df.to_csv('data/employee_sales_clean.csv',index=False)

print('Data preprocessing completed')