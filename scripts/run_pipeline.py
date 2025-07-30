# scripts/run_pipeline.py

from extract.extract_orders import extract_orders
from transform.clean_orders import clean_orders
from load.load_to_s3 import upload_to_s3
from load.load_to_snowflake import load_to_snowflake

def run():
    print("Starting SnapBuy data pipeline...\n")

    try:
        print("[1/4] Extracting data from PostgreSQL...")
        extract_orders()
        print("Data extraction completed successfully.\n")

        print("[2/4] Transforming and cleaning data...")
        clean_orders()
        print("Data transformation completed successfully.\n")

        print("[3/4] Uploading data to AWS S3...")
        upload_to_s3()
        print("Data uploaded to S3 successfully.\n")

        print("[4/4] Loading data into Snowflake...")
        load_to_snowflake()
        print("Data loaded into Snowflake successfully.\n")

        print("Pipeline execution completed successfully.")

    except Exception as e:
        print(f"Pipeline execution failed with error: {e}")

if __name__ == '__main__':
    run()
