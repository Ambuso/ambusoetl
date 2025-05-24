import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'dbname': os.getenv("DB_NAME"),
    'host': os.getenv("DB_HOST"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'port': int(os.getenv("DB_PORT")) if os.getenv("DB_PORT") else None,
}

def create_table_if_not_exists(cursor):
    cursor.execute("CREATE SCHEMA IF NOT EXISTS assignment;")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assignment.weather_data (
            id SERIAL PRIMARY KEY,
            city TEXT NOT NULL,
            temperature FLOAT NOT NULL,
            description TEXT,
            humidity INT
        );
    """)

def insert_weather_data(cursor, city, temperature, description, humidity):
    cursor.execute("""
        INSERT INTO assignment.weather_data (city, temperature, description, humidity)
        VALUES (%s, %s, %s, %s);
    """, (city, temperature, description, humidity))

def load_data(df):
    if df.empty:
        raise ValueError("Empty DataFrame passed to load_data")

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            create_table_if_not_exists(cursor)
            row = df.iloc[0]
            insert_weather_data(cursor, row['City'], row['Temperature'], row['Description'], row['Humidity'])
        conn.commit()
