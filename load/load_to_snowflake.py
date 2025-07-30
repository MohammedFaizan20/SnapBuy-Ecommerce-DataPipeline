# load/load_to_snowflake.py

import os
import snowflake.connector
import glob
from datetime import datetime

def load_to_snowflake():
    """
    Loads the most recent cleaned order CSV file into a Snowflake staging table.
    Assumes Snowflake stage, file format, and table are preconfigured.
    """
    try:
        # Connect to Snowflake
        conn = snowflake.connector.connect(
            user=os.getenv("SNOWFLAKE_USER", "snapbuy_user"),
            password=os.getenv("SNOWFLAKE_PASSWORD", "snapbuy_pass"),
            account=os.getenv("SNOWFLAKE_ACCOUNT", "xy12345.ap-southeast-1"),
            warehouse=os.getenv("SNOWFLAKE_WAREHOUSE", "COMPUTE_WH"),
            database=os.getenv("SNOWFLAKE_DATABASE", "SNAPBUY_DWH"),
            schema=os.getenv("SNOWFLAKE_SCHEMA", "PUBLIC")
        )

        cs = conn.cursor()

        # Locate the latest cleaned file
        cleaned_files = sorted(glob.glob("/tmp/orders_cleaned_*.csv"), reverse=True)
        if not cleaned_files:
            raise FileNotFoundError("No cleaned orders CSV file found in /tmp")

        local_file_path = cleaned_files[0]
        stage_name = "@snapbuy_stage"
        target_table = "STG_ORDERS"
        file_format = "(type = 'CSV' field_delimiter=',' skip_header=1)"

        # Upload file to Snowflake stage
        put_command = f"PUT file://{local_file_path} {stage_name} OVERWRITE = TRUE"
        cs.execute(put_command)

        # Load data into table from stage
        copy_command = f"COPY INTO {target_table} FROM {stage_name} FILE_FORMAT = {file_format}"
        cs.execute(copy_command)

        print(f"Data from {os.path.basename(local_file_path)} loaded into Snowflake table '{target_table}'")

    except Exception as e:
        raise RuntimeError(f"Failed to load data into Snowflake: {e}")

    finally:
        if 'cs' in locals():
            cs.close()
        if 'conn' in locals():
            conn.close()
