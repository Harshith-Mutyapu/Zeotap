from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

# Path to the SQLite database
db_path = r"C:\Users\harsh\OneDrive\Desktop\ZEOTAP ASSESSMENT\APPLICATION 2\database\weather_data.db"

@app.route('/')
def index():
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch distinct weather data (unique city and date combinations)
    cursor.execute('''
        SELECT DISTINCT city, date, temperature, feels_like, weather_condition, 
            humidity, wind_speed, pressure, sunrise, sunset
        FROM weather_data
    ''')

    weather_data = cursor.fetchall()
    conn.close()

    # Pass data to template
    return render_template('index.html', weather_data=weather_data)

def store_to_db(daily_summary):
    # Check if the database exists
    if not os.path.exists(db_path):
        print(f"Database file does not exist at {db_path}")
        return

    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Check if the data for the same city and date already exists
    cursor.execute('''
        SELECT * FROM weather_data
        WHERE city = ? AND date = ?
    ''', (daily_summary['city'], daily_summary['date']))

    existing_data = cursor.fetchall()
    if existing_data:
        print(f"Data already exists for {daily_summary['city']} on {daily_summary['date']}")
        conn.close()
        return

    # Insert the weather data into the database
    cursor.execute(''' 
        INSERT INTO weather_data (
            city, date, temperature, feels_like, weather_condition,
            humidity, wind_speed, pressure, sunrise, sunset
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) 
    ''', (
        daily_summary['city'],
        daily_summary['date'],
        daily_summary['temperature'],
        daily_summary['feels_like'],
        daily_summary['weather_condition'],
        daily_summary['humidity'],
        daily_summary['wind_speed'],
        daily_summary['pressure'],
        daily_summary['sunrise'],
        daily_summary['sunset']
    ))

    conn.commit()
    conn.close()

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
