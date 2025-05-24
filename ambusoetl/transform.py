import pandas as pd

def transform_weather_data(weather_json):
    if not weather_json:
        raise ValueError("No weather data to transform")

    data = {
        'City': weather_json.get('name'),
        'Temperature': weather_json.get('main', {}).get('temp'),
        'Description': weather_json.get('weather', [{}])[0].get('description'),
        'Humidity': weather_json.get('main', {}).get('humidity'),
    }
    df = pd.DataFrame([data])
    return df
