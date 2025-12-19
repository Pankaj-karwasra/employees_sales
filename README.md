📊 Employee Sales Data Analysis Pipeline
📌 Overview

This project demonstrates an end-to-end data analysis pipeline using Python and SQL.
The pipeline ingests raw employee sales data, performs data cleaning and preprocessing, stores the cleaned data in a SQLite database, and runs SQL-based analysis.

🧰 Tech Stack

Python

Pandas

SQLite

SQL



📁 Project Structure
employee_sales_pipeline/
├── data/
│   ├── employee_sales_raw.csv
│   └── employee_sales_clean.csv
├── database/
│   └── company.db
├── scripts/
│   ├── load_raw_data.py
│   ├── preprocess_data.py
│   ├── load_clean_data.py
│   ├── analysis.py
│   └── pipeline.py

⚙️ How It Works

Load raw CSV data into SQLite

Clean duplicates and missing values using Pandas

Store cleaned data in the database

Perform SQL analysis

Run the complete pipeline using a single script

▶️ Run the Project
pip install pandas
python scripts/pipeline.py

📈 Analysis Includes

Average salary by department

Top sales-performing employee

Employees with high experience

🎯 Purpose

This project is built for learning and demonstration of real-world data preprocessing, SQL analysis, and pipeline automation.
