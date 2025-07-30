# SnapBuy — E-Commerce Data Pipeline & Analytics Platform

## Project Overview
SnapBuy is a full-stack Data Engineering project simulating a production-grade ETL pipeline for an e-commerce platform. It demonstrates the automation of data extraction, transformation, loading, and modeling using modern data tools. The goal is to enable real-time insights into key business metrics such as sales performance, revenue trends, and customer behavior.

This project simulates how an e-commerce business would build an end-to-end data pipeline using Python, PostgreSQL, Apache Airflow, AWS S3, and Snowflake.

---

## Technologies Used

| Tool/Service        | Purpose                                      |
|---------------------|----------------------------------------------|
| Python              | ETL scripting and logic                      |
| PostgreSQL          | Source database storing raw transactional data |
| Apache Airflow      | Workflow orchestration of ETL steps          |
| AWS S3              | Cloud storage for raw/cleaned files          |
| Snowflake           | Cloud data warehouse for analytics           |
| Snowpipe (simulated)| Auto-loading cleaned data from S3 to Snowflake |
| GitHub Actions      | CI/CD automation (lint checks, deployment)   |

---

## Project Workflow

### 1. Data Source
- Raw transactional data such as `orders` and `payments` are stored in PostgreSQL.

### 2. ETL Orchestration (via Airflow)
The pipeline runs in 4 stages:
- **Extract**: Pull order and payment data from PostgreSQL and write to CSV
- **Transform**: Clean and standardize the extracted data
- **Load to S3**: Archive cleaned CSV files to AWS S3
- **Load to Snowflake**: Load data from S3 to Snowflake using `PUT` and `COPY INTO`

### 3. Data Modeling (Star Schema)
Structured Snowflake tables include:
- `fact_orders` — transaction facts
- `dim_user`, `dim_product`, `dim_date` — supporting dimensions

### 4. Testing and Reliability
- PostgreSQL, S3, and Snowflake connections are validated with test scripts.
- Clean exception handling is used throughout the pipeline.

---

## 🗂️ Project Structure

```
SnapBuy-Ecommerce-DataPipeline/
├── airflow_dags/               # Airflow DAG definition
├── extract/                    # Python scripts to extract data
├── transform/                  # Data cleaning and transformation logic
├── load/                       # Load logic for S3 and Snowflake
├── test/                       # Test scripts for Postgres, S3, and Snowflake
├── sql/                        # SQL scripts for schema and seed data
├── scripts/                    # Master script to simulate local ETL execution
├── .github/workflows/          # GitHub Actions CI/CD workflow
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git exclusions
└── README.md                   # Project documentation
```

---

## 🧪 Testing Utilities

You can run connection tests individually:
```bash
python test/test_postgres_connection.py
python test/test_s3_upload.py
python test/test_snowflake_connection.py
```

Or run the full pipeline locally:
```bash
python scripts/run_pipeline.py
```

---

## Sample Data

Found in `sql/sample_data.sql`, the project includes sample:
- Users, Products, Dates
- Orders joined with payment information

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/SnapBuy-Ecommerce-DataPipeline.git
cd SnapBuy-Ecommerce-DataPipeline
```

### 2. Set up Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file or set the following:
```env
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=snapbuy_user
POSTGRES_PASSWORD=snapbuy_pass
POSTGRES_DB=snapbuy_db

S3_BUCKET_NAME=snapbuy-data-lake
S3_OBJECT_PREFIX=orders/cleaned/

SNOWFLAKE_USER=snapbuy_user
SNOWFLAKE_PASSWORD=snapbuy_pass
SNOWFLAKE_ACCOUNT=xy12345.ap-southeast-1
SNOWFLAKE_WAREHOUSE=COMPUTE_WH
SNOWFLAKE_DATABASE=SNAPBUY_DWH
SNOWFLAKE_SCHEMA=PUBLIC
SNOWFLAKE_STAGE=@snapbuy_stage
SNOWFLAKE_TARGET_TABLE=STG_ORDERS
```

---

## 📊 Dashboards (Optional)
If integrating Power BI dashboards in the future, connect to Snowflake and visualize:
- Total Sales
- Revenue Trends
- Product Performance
- Cart Abandonment

---

## Created By
**Mohammed Faizan**  
[LinkedIn](https://www.linkedin.com/in/mohammedfaizan20)  •  [GitHub](https://github.com/MohammedFaizan20)

---

## 🙋‍♂️ Contact
Feel free to reach out via LinkedIn or GitHub if you have any questions or feedback!
