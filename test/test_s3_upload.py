# test/test_s3_upload.py

import boto3
import os
from botocore.exceptions import ClientError

def test_s3_upload():
    """
    Tests the ability to upload a dummy file to the configured AWS S3 bucket.
    Useful for validating AWS credentials and bucket permissions.
    """
    try:
        s3 = boto3.client('s3')
        bucket_name = os.getenv("S3_BUCKET_NAME", "snapbuy-data-lake")
        test_file_path = "/tmp/s3_test_file.txt"

        # Write test content
        with open(test_file_path, "w") as f:
            f.write("S3 upload connectivity test.")

        # Upload test file
        s3.upload_file(test_file_path, bucket_name, "test/s3_test_file.txt")
        print(f"Test file uploaded successfully to S3 bucket '{bucket_name}'.")

    except ClientError as e:
        print(f"S3 upload test failed: {e}")

    except Exception as e:
        print(f"Unexpected error during S3 upload test: {e}")

if __name__ == '__main__':
    test_s3_upload()
