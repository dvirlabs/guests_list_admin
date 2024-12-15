import psycopg2
from psycopg2.extras import RealDictCursor


def connect_to_db():
    conn = psycopg2.connect(
        host="localhost",
        port="5433",
        database="orders_db",
        user="postgres",
        password="Aa123456"
    )
    return conn

def close_db(conn):
    conn.close()

def get_todo_table():
    connection = None
    try:
        connection = connect_to_db()
        with connection.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM orders ORDER BY id ASC")
            rows = cur.fetchall()
            return rows
    except Exception as e:
        print(f"Error fetching data from the database: {e}")
        return []
    finally:
        if connection:
            connection.close()

def insert_order(first_name, last_name, phone, status, how_much):
    connection = None
    try:
        connection = connect_to_db()
        with connection.cursor() as cur:
            cur.execute("INSERT INTO orders (first_name, last_name, phone, status, how_much) VALUES (%s, %s, %s, %s, %s)", (first_name, last_name, phone, status, how_much))
            connection.commit()
        return {"message": "order added successfully"}
    except Exception as e:
        print(f"Error inserting data into the database: {e}")
        return {"error": "Error inserting order"}
    finally:
        if connection:
            connection.close()