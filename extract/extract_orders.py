# extract/extract_orders.py

import psycopg2
import pandas as pd
import os
from datetime import datetime

def extract_orders():
    """
    Connects to PostgreSQL database and extracts order and payment data into a CSV file.
    The output CSV is saved under the /tmp directory with a timestamp.
    """
    try:
        connection = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST", "localhost"),
            port=os.getenv("POSTGRES_PORT", "5432"),
            user=os.getenv("POSTGRES_USER", "snapbuy_user"),
            password=os.getenv("POSTGRES_PASSWORD", "snapbuy_pass"),
            dbname=os.getenv("POSTGRES_DB", "snapbuy_db")
        )

        query = """
            SELECT o.order_id, o.order_date, o.user_id, o.product_id, o.quantity, o.total_amount,
                   p.payment_method, p.payment_status
            FROM orders o
            JOIN payments p ON o.order_id = p.order_id;
        """

        df = pd.read_sql(query, connection)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"/tmp/orders_{timestamp}.csv"
        df.to_csv(output_path, index=False)

        print(f"Extracted data written to {output_path}")

    except Exception as e:
        raise RuntimeError(f"Error extracting data from PostgreSQL: {e}")

    finally:
        if 'connection' in locals():
            connection.close()
