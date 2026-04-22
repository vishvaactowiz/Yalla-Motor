import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "actowiz",
    "database": "yalla_motor"
}

def create_table():
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS kia_dealers (
            state_name VARCHAR(100),
            state_code VARCHAR(20),
            city_name VARCHAR(100),
            city_code VARCHAR(20),
            id VARCHAR(50),
            store_name VARCHAR(255),
            dealer_type VARCHAR(100),
            phone1 VARCHAR(30),
            url TEXT,
            full_address TEXT
        )
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Table created")


def insert_data(rows):
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()

    insert_query = """
        INSERT INTO kia_dealers
        (state_name, state_code, city_name, city_code, id, store_name,
         dealer_type, phone1, url, full_address)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    cur.executemany(insert_query, rows)

    conn.commit()
    cur.close()
    conn.close()

    print("Inserted:", len(rows))