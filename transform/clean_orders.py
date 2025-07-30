# transform/clean_orders.py

import pandas as pd
import os
import glob
from datetime import datetime

def clean_orders():
    """
    Cleans the most recent extracted order data from /tmp.
    Performs basic validation, missing value handling, and data type formatting.
    Saves the cleaned data as a new CSV file.
    """
    try:
        # Find the most recent extracted file
        extracted_files = sorted(glob.glob("/tmp/orders_*.csv"), reverse=True)
        if not extracted_files:
            raise FileNotFoundError("No extracted orders CSV found in /tmp")

        input_path = extracted_files[0]
        df = pd.read_csv(input_path)

        # Clean and transform
        df.dropna(subset=['order_id', 'user_id', 'product_id', 'total_amount'], inplace=True)
        df['order_date'] = pd.to_datetime(df['order_date'])
        df['quantity'] = df['quantity'].astype(int)
        df['total_amount'] = df['total_amount'].astype(float)
        df['payment_status'] = df['payment_status'].str.lower().str.strip()
        df['payment_method'] = df['payment_method'].str.title().str.strip()

        # Output cleaned file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"/tmp/orders_cleaned_{timestamp}.csv"
        df.to_csv(output_path, index=False)

        print(f"Cleaned data written to {output_path}")

    except Exception as e:
        raise RuntimeError(f"Error cleaning order data: {e}")
