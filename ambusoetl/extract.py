import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("api_key")
CITY_NAME = os.getenv("CITY_NAME", "Nairobi")

def fetch_weather():
    if not API_KEY:
        raise ValueError("API_KEY missing in environment variables")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"API request failed: {response.status_code} - {response.text}")
    return response.json()
