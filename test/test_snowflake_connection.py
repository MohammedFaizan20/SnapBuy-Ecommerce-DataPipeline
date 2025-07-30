# test/test_snowflake_connection.py

import snowflake.connector
import os

def test_snowflake_connection():
    """
    Tests connection to the Snowflake data warehouse by running a basic SELECT statement.
    """
    try:
        conn = snowflake.connector.connect(
            user=os.getenv("SNOWFLAKE_USER", "snapbuy_user"),
            password=os.getenv("SNOWFLAKE_PASSWORD", "snapbuy_pass"),
            account=os.getenv("SNOWFLAKE_ACCOUNT", "xy12345.ap-southeast-1"),
            warehouse=os.getenv("SNOWFLAKE_WAREHOUSE", "COMPUTE_WH"),
            database=os.getenv("SNOWFLAKE_DATABASE", "SNAPBUY_DWH"),
            schema=os.getenv("SNOWFLAKE_SCHEMA", "PUBLIC")
        )

        cs = conn.cursor()
        cs.execute("SELECT CURRENT_VERSION();")
        version = cs.fetchone()

        print(f"Snowflake connection test passed. Current version: {version[0]}")

    except Exception as e:
        print(f"Snowflake connection test failed: {e}")

    finally:
        if 'cs' in locals():
            cs.close()
        if 'conn' in locals():
            conn.close()

if __name__ == '__main__':
    test_snowflake_connection()
