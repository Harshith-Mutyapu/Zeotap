from flask import Flask, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Function to fetch weather data from the SQLite database
def fetch_weather_data():
    conn = sqlite3.connect('database/weather_data.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM weather_data ORDER BY date DESC LIMIT 10;")
    weather_records = cursor.fetchall()
    
    conn.close()
    return weather_records

# Route to display weather data
@app.route('/')
def index():
    weather_data = fetch_weather_data()
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
