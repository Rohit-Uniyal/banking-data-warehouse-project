# Banking Data Warehouse Project

## Project Overview

This project demonstrates the design and implementation of an end-to-end Banking Data Warehouse using Python and PostgreSQL.

The solution simulates a real-world banking environment by generating customer, account, and transaction data, loading it into a staging layer, transforming it through ETL pipelines, and building a dimensional warehouse using Star Schema modeling.

---

## Business Problem

Banks generate large volumes of transactional data daily.

Business users require answers to questions such as:

- Which customers have the highest balances?
- What is the total transaction volume by month?
- Which account types generate the most transactions?
- How do transaction trends change over time?

A Data Warehouse enables fast analytical reporting and business intelligence.

---

## Architecture

```text
Raw CSV Files
│
├── customers.csv
├── accounts.csv
└── transactions.csv

        ↓

Python ETL
----------
extract.py
transform.py
load.py

        ↓

PostgreSQL Staging Layer
------------------------
customer_test
account_test
transaction_test

        ↓

Warehouse ETL
-------------
warehouse_loader.py

        ↓

Star Schema
-----------
dim_customer
dim_account
dim_date
fact_transaction

        ↓

Analytics / Reporting
---------------------
Power BI
Tableau
```

---

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQL
- Git
- GitHub

Future Enhancements:

- Apache Airflow
- Power BI Dashboard
- Docker
- Cloud Deployment

---

## Dataset

Synthetic banking data generated using Python.

### Customers

- Customer ID
- Customer Name
- City
- Phone
- Annual Income

### Accounts

- Account ID
- Customer ID
- Account Type
- Balance

### Transactions

- Transaction ID
- Account ID
- Transaction Type
- Amount
- Transaction Date

---

## ETL Process

### Extract

Data is extracted from CSV files using Pandas.

### Transform

Data quality checks:

- Remove null values
- Remove duplicates
- Standardize data types

### Load

Data is loaded into PostgreSQL staging tables.

---

## Data Warehouse Design

### Dimension Tables

#### dim_customer

Stores customer-related attributes.

#### dim_account

Stores account information.

#### dim_date

Stores date hierarchy information.

---

### Fact Table

#### fact_transaction

Stores transactional measures:

- Transaction Amount
- Transaction Type

Links to:

- Customer Dimension
- Account Dimension
- Date Dimension

---

## Star Schema

```text
                 dim_customer
                       |
                       |
                       |
dim_date ---- fact_transaction ---- dim_account
```

---

## Features Implemented

- End-to-End ETL Pipeline
- Data Warehouse Design
- Star Schema Modeling
- Fact and Dimension Tables
- Logging
- Error Handling
- Bulk Data Loading
- Git Version Control

---

## Project Structure

```text
Banking-Data-Engineering-Project
│
├── data
│   └── raw
│       ├── customers.csv
│       ├── accounts.csv
│       └── transactions.csv
│
├── python
│   └── etl
│       ├── config.py
│       ├── extract.py
│       ├── transform.py
│       ├── load.py
│       ├── logger.py
│       ├── main.py
│       ├── warehouse_loader.py
│       └── warehouse_main.py
│
├── logs
│
├── .gitignore
│
└── README.md
```

---

## How To Run

### Run Staging ETL

```bash
python main.py
```

### Run Warehouse ETL

```bash
python warehouse_main.py
```

---

## Future Improvements

- Apache Airflow Orchestration
- Power BI Dashboard
- Docker Containerization
- AWS Deployment
- Incremental Loading
- Data Quality Framework

---

## Author

Rohit Uniyal

GitHub:
https://github.com/Rohit-Uniyal
