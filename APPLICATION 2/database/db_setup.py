import sqlite3
import os

def create_database():
    db_path = r"C:\Users\harsh\OneDrive\Desktop\ZEOTAP ASSESSMENT\APPLICATION 2\database\weather_data.db"
    
    # Check if the database file exists
    if os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Drop the table if it exists
        cursor.execute("DROP TABLE IF EXISTS weather_data;")
        conn.commit()

        # Create the table for storing weather data with a UNIQUE constraint on (city, date)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            date TEXT NOT NULL,
            temperature REAL,
            feels_like REAL,
            weather_condition TEXT,
            humidity INTEGER,
            wind_speed REAL,
            pressure INTEGER,
            sunrise INTEGER,
            sunset INTEGER,
            UNIQUE(city, date)  -- Ensuring no duplicates for (city, date)
        );
        ''')
        
        conn.commit()
        conn.close()
        print(f"Database and table recreated at {db_path}")
    else:
        print(f"Database file does not exist at {db_path}")

def store_to_db(weather_data):
    db_path = r"C:\Users\harsh\OneDrive\Desktop\ZEOTAP ASSESSMENT\APPLICATION 2\database\weather_data.db"
    
    try:
        # Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # First, check if a record with the same city and date already exists
        cursor.execute('''
        SELECT 1 FROM weather_data WHERE city = ? AND date = ?
        ''', (weather_data['city'], weather_data['date']))
        existing_record = cursor.fetchone()

        if existing_record:
            print(f"Duplicate record found for {weather_data['city']} on {weather_data['date']}. Skipping insertion.")
        else:
            # Insert new record if no existing record found
            cursor.execute('''
            INSERT INTO weather_data (
                city, 
                date, 
                temperature, 
                feels_like, 
                weather_condition, 
                humidity, 
                wind_speed, 
                pressure, 
                sunrise, 
                sunset
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                weather_data['city'],
                weather_data['date'],
                weather_data['temperature'],
                weather_data['feels_like'],
                weather_data['weather_condition'],
                weather_data['humidity'],
                weather_data['wind_speed'],
                weather_data['pressure'],
                weather_data['sunrise'],
                weather_data['sunset']
            ))

            # Commit the changes and close the connection
            conn.commit()
            print("Data inserted successfully.")
        
        # Close connection
        conn.close()
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

# Create the database and table
if __name__ == "__main__":
    create_database()

    # Example weather data to insert
    weather_data = {
        'city': 'London',
        'date': '2024-10-18',
        'temperature': 14.18,
        'feels_like': 13.65,
        'weather_condition': 'few clouds',
        'humidity': 76,
        'wind_speed': 3.6,
        'pressure': 1013,
        'sunrise': 1729232995,
        'sunset': 1729270856
    }

    # Store data in the database
    store_to_db(weather_data)
