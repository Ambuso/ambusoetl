# ambusoetl
# 🌦️ Weather ETL Pipeline Project
This is a simple ETL (Extract, Transform, Load) pipeline that fetches real-time weather data from the OpenWeatherMap API and stores it in a PostgreSQL database. The script is written in Python and leverages the requests, pandas, and psycopg2 libraries.

# 🛠 Features
Extracts current weather data (temperature, humidity, description, and city name) from the OpenWeatherMap API.
Transforms the data into a clean and structured format using a pandas DataFrame.
Loads the data into a PostgreSQL table within a schema named assignment.
Automatically creates the required schema and table if they don’t exist.

# 📦 Project Structure
weather_etl_project/
│
├── weather_etl.py        # Main ETL script
├── .env                  # Environment variables (not committed)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

# ⚙️ Setup Instructions
## 1. Clone the repository
git clone https://github.com/your-username/weather-etl-project.git
cd weather-etl-project

## 2. Install dependencies
pip install -r requirements.txt

## 3. Create a .env file
Create a .env file in the project root and add the following environment variables:
API_KEY=your_openweathermap_api_key
CITY_NAME=Nairobi
DB_NAME=your_db_name
DB_HOST=your_db_host
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_PORT=5432

## 4. Run the ETL script
python weather_etl.py

# 🧪 Sample Output
Weather DataFrame:
     City  Temperature    Description  Humidity
0  Nairobi         25.6  scattered clouds       65

Weather data inserted successfully into PostgreSQL.

# 🗃️ PostgreSQL Table Schema
Table: assignment.weather_data

| Column      | Type   | Description            |
| ----------- | ------ | ---------------------- |
| id          | SERIAL | Primary key            |
| city        | TEXT   | City name              |
| temperature | FLOAT  | Temperature in Celsius |
| description | TEXT   | Weather description    |
| humidity    | INT    | Humidity percentage    |

# ✅ Dependencies
Dependencies
Python 3.7+
requests
pandas
psycopg2
python-dotenv

# 👤 Author
Name: Ambuso Dismas
Role: Data Engineer
GitHub: ambuso
Blog:https://dev.to/dismas_mike
Email: dismasmik3@gmail.com

# 📄 License
This project is licensed under the MIT License.

# 🤝 Contributions
Pull requests are welcome!
If you'd like to suggest a feature or report a bug, please open an issue on GitHub.







