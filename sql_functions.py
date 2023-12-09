#Use SQLite3 to create a local database and save the scraped values in the table.
import sqlite3
from datetime import datetime, timedelta

def create_table_if_not_exists():
    conn = sqlite3.connect('gas_prices_database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sqlite_master WHERE type='table' AND name='gas_prices'")
    table_exists = cursor.fetchone()

    if not table_exists:
        cursor.execute('''
                    CREATE TABLE gas_prices (
                       state TEXT PRIMARY KEY,
                       regular REAL,
                       midgrade REAL,
                       premium REAL,
                       diesel REAL,
                       date_updated TEXT
                    )
                       ''')
        conn.commit()
        print("Table Created.")
    else:
        print("Table already exists.")
    conn.close()

create_table_if_not_exists()
    

