# Banking Data Warehouse & Analytics Platform

## Project Overview

This project demonstrates the design and implementation of an end-to-end Banking Data Warehouse using Python, PostgreSQL, Apache Airflow, Docker, and Power BI.

The solution simulates a real-world banking environment by generating customer, account, and transaction data, loading it into a staging layer, transforming it through ETL pipelines, and building a dimensional data warehouse using Star Schema modeling for analytics and reporting.

---

## Business Problem

Banks generate large volumes of transactional data daily. Business users require fast access to analytical insights to support decision-making.

Typical business questions include:

* Which customers maintain the highest balances?
* What is the monthly transaction volume?
* Which account types generate the most activity?
* How do transaction trends change over time?
* Which cities contribute the highest banking revenue?

A Data Warehouse enables efficient reporting, trend analysis, and business intelligence.

---

## Project Architecture

```text
Raw Data Generation
-------------------
customers.csv
accounts.csv
transactions.csv

        ↓

Python ETL Pipeline
-------------------
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

Star Schema Data Warehouse
--------------------------
dim_customer
dim_account
dim_date
fact_transaction

        ↓

Analytics Layer
---------------
Power BI Dashboard

        ↑

Apache Airflow
(Workflow Orchestration)
```

---

## End-to-End Workflow

```text
Generate Banking Data
        ↓
Raw CSV Files
        ↓
Python ETL Pipeline
        ↓
PostgreSQL Staging Layer
        ↓
Warehouse ETL
        ↓
Star Schema Data Warehouse
        ↓
Power BI Dashboard
        ↑
Apache Airflow Orchestration
```

---

## Tech Stack

### Data Engineering

* Python
* Pandas
* PostgreSQL
* SQL

### Workflow Orchestration

* Apache Airflow

### Containerization

* Docker
* Docker Compose

### Visualization

* Power BI

### Version Control

* Git
* GitHub

---

## Dataset

Synthetic banking data generated using Python and Faker.

### Customer Data

* Customer ID
* Customer Name
* City
* Phone Number
* Annual Income

### Account Data

* Account ID
* Customer ID
* Account Type
* Balance

### Transaction Data

* Transaction ID
* Account ID
* Transaction Type
* Amount
* Transaction Date

---

## ETL Pipeline

### Extract

Data is extracted from raw CSV files using Pandas.

### Transform

Data quality checks performed:

* Null value handling
* Duplicate removal
* Data type validation
* Standardization

### Load

Processed data is loaded into PostgreSQL staging tables.

---

## Data Warehouse Design

### Dimension Tables

#### dim_customer

Stores customer attributes.

#### dim_account

Stores account-related information.

#### dim_date

Stores date hierarchy for time-based analysis.

### Fact Table

#### fact_transaction

Stores transaction measures and business metrics.

Measures:

* Transaction Amount
* Transaction Count

Relationships:

* Customer Dimension
* Account Dimension
* Date Dimension

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

## Apache Airflow Orchestration

The ETL process is automated using Apache Airflow.

### DAG Workflow

```text
run_etl
    ↓
load_warehouse
```

Airflow provides:

* Workflow orchestration
* Task scheduling
* Dependency management
* Logging and monitoring
* Error handling

---

## Docker Containerization

Docker is used to provide a consistent development and deployment environment.

### Containers Used

* PostgreSQL Database
* Apache Airflow Webserver
* Apache Airflow Scheduler

Docker Compose manages all services and networking.

---

## Power BI Dashboard

The Power BI dashboard provides insights into:

* Customer demographics
* Account distribution
* Transaction trends
* Revenue analysis
* Banking performance metrics

---

## Project Features

* End-to-End ETL Pipeline
* Data Warehouse Design
* Star Schema Modeling
* PostgreSQL Database
* Apache Airflow Orchestration
* Docker Containerization
* Power BI Dashboard
* Logging & Monitoring
* Error Handling
* Git Version Control

---

## Project Structure

```text
Banking-Data-Engineering-Project
│
├── airflow
│   ├── dags
│   ├── logs
│   └── docker-compose.yml
│
├── data
│   └── raw
│       ├── customers.csv
│       ├── accounts.csv
│       └── transactions.csv
│
├── docker
│   └── docker-compose.yml
│
├── python
│   ├── generate_customers.py
│   ├── generate_accounts.py
│   ├── generate_transactions.py
│   └── etl
│       ├── extract.py
│       ├── transform.py
│       ├── load.py
│       ├── main.py
│       ├── warehouse_loader.py
│       └── warehouse_main.py
│
├── power bi
│
├── screenshots
│
├── sql
│
├── README.md
│
└── .gitignore
```

---

## How to Run

### Generate Data

```bash
python generate_customers.py
python generate_accounts.py
python generate_transactions.py
```

### Run ETL Pipeline

```bash
python python/etl/main.py
```

### Load Data Warehouse

```bash
python python/etl/warehouse_main.py
```

### Start Airflow

```bash
cd airflow
docker compose up -d
```

### Access Airflow

```text
http://localhost:8081
```

---

## Screenshots

### Airflow DAG

(Add screenshot)

### Power BI Dashboard

(Add screenshot)

### Docker Containers

(Add screenshot)

### PostgreSQL Warehouse Tables

(Add screenshot)

---

## Future Enhancements

* AWS Deployment
* Incremental Data Loading
* CI/CD Pipeline
* Data Quality Validation Framework
* Real-Time Data Streaming with Kafka
* Snowflake Data Warehouse Integration

---

## Author

**Rohit Uniyal**

GitHub:
https://github.com/Rohit-Uniyal

LinkedIn:
(Add LinkedIn Profile URL)
