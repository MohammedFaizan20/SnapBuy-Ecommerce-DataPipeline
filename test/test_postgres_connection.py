# test/test_postgres_connection.py

import psycopg2
import os

def test_postgres_connection():
    """
    Tests connectivity to the PostgreSQL source database used for extracting order data.
    """
    try:
        conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST", "localhost"),
            port=os.getenv("POSTGRES_PORT", "5432"),
            user=os.getenv("POSTGRES_USER", "snapbuy_user"),
            password=os.getenv("POSTGRES_PASSWORD", "snapbuy_pass"),
            dbname=os.getenv("POSTGRES_DB", "snapbuy_db")
        )

        cur = conn.cursor()
        cur.execute("SELECT 1;")
        result = cur.fetchone()

        assert result[0] == 1
        print("PostgreSQL connection test passed.")

    except Exception as e:
        print(f"PostgreSQL connection test failed: {e}")

    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

if __name__ == '__main__':
    test_postgres_connection()
