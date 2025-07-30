# load/load_to_s3.py

import boto3
import os
import glob
from datetime import datetime

def upload_to_s3():
    """
    Uploads the most recent cleaned orders CSV from /tmp to a designated S3 bucket.
    Assumes AWS credentials are configured in the environment or via IAM role.
    """
    try:
        s3_client = boto3.client('s3')
        bucket_name = os.getenv("S3_BUCKET_NAME", "snapbuy-data-lake")
        s3_prefix = os.getenv("S3_OBJECT_PREFIX", "orders/cleaned/")

        # Locate most recent cleaned file
        cleaned_files = sorted(glob.glob("/tmp/orders_cleaned_*.csv"), reverse=True)
        if not cleaned_files:
            raise FileNotFoundError("No cleaned orders CSV found in /tmp")

        local_file_path = cleaned_files[0]
        file_name = os.path.basename(local_file_path)
        s3_key = f"{s3_prefix}{file_name}"

        s3_client.upload_file(local_file_path, bucket_name, s3_key)

        print(f"Uploaded {file_name} to S3 bucket '{bucket_name}' at '{s3_key}'")

    except Exception as e:
        raise RuntimeError(f"Failed to upload cleaned data to S3: {e}")
