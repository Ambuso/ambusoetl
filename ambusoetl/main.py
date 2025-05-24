import requests
import os
from dotenv import load_dotenv
import pandas as pd
import psycopg2

# Load environment variables
load_dotenv()

# Weather API setup
city_name = os.getenv("CITY_NAME", "Nairobi")
API_key = os.getenv("API_KEY")
weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"

# PostgreSQL connection details from environment
db_name = os.getenv("DB_NAME")
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_port = int(os.getenv("DB_PORT")) if os.getenv("DB_PORT") else None

# Fetch weather data
response = requests.get(weather_url)

if response.status_code == 200:
    try:
        weather_data = response.json()
        city = weather_data['name']
        description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        temperature = weather_data['main']['temp']

        # Create DataFrame
        df = pd.DataFrame({
            'City': [city],
            'Temperature': [temperature],
            'Description': [description],
            'Humidity': [humidity]
        })
        print("Weather DataFrame:")
        print(df)

        # Connect to PostgreSQL
        conn = psycopg2.connect(
            dbname=db_name,
            host=db_host,
            user=db_user,
            password=db_password,
            port=db_port,
        )
        curr = conn.cursor()

        # Create schema and table if they do not exist
        curr.execute("CREATE SCHEMA IF NOT EXISTS assignment;")
        curr.execute("""
            CREATE TABLE IF NOT EXISTS assignment.weather_data (
                id SERIAL PRIMARY KEY,
                city TEXT,
                temperature FLOAT,
                description TEXT,
                humidity INT
            );
        """)

        # Insert weather data into table
        curr.execute("""
            INSERT INTO assignment.weather_data (city, temperature, description, humidity)
            VALUES (%s, %s, %s, %s);
        """, (city, temperature, description, humidity))

        conn.commit()
        print("Weather data inserted successfully into PostgreSQL.")

    except Exception as e:
        print(f"Error processing or inserting data: {e}")
    finally:
        if conn:
            curr.close()
            conn.close()
else:
    print(f"Failed to fetch weather data: {response.status_code} - {response.text}")
