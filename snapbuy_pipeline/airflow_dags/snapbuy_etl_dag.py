# airflow_dags/snapbuy_etl_dag.py

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from extract.extract_orders import extract_orders
from transform.clean_orders import clean_orders
from load.load_to_s3 import upload_to_s3
from load.load_to_snowflake import load_to_snowflake

default_args = {
    'owner': 'faizan',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'snapbuy_etl_pipeline',
    default_args=default_args,
    description='ETL pipeline for SnapBuy e-commerce data',
    schedule_interval='@daily',
    start_date=datetime(2024, 5, 1),
    catchup=False,
    tags=['snapbuy', 'ecommerce', 'etl']
)

extract_task = PythonOperator(
    task_id='extract_orders',
    python_callable=extract_orders,
    dag=dag
)

transform_task = PythonOperator(
    task_id='clean_orders',
    python_callable=clean_orders,
    dag=dag
)

upload_task = PythonOperator(
    task_id='upload_to_s3',
    python_callable=upload_to_s3,
    dag=dag
)

load_task = PythonOperator(
    task_id='load_to_snowflake',
    python_callable=load_to_snowflake,
    dag=dag
)

extract_task >> transform_task >> upload_task >> load_task
