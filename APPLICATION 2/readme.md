# Weather Data Processing and Storage Application

This project is a weather data processing web application that retrieves weather data using the OpenWeatherMap API and stores it in an SQLite database. It ensures that no duplicate records are stored in the database and allows users to view the weather data on a web page.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [API Details](#api-details)
- [Technologies](#technologies)
- [License](#license)

## Features
- Fetches real-time weather data from the OpenWeatherMap API.
- Stores weather data in an SQLite database with unique city-date combinations to prevent duplicates.
- Displays weather information in a simple HTML table format.
- Implements basic routing with Flask to render the weather data on a web page.

## Project Structure

```bash
├── app.py                 # Main Flask application file
├── database
│   └── weather_data.db     # SQLite database file
├── templates
│   └── index.html          # HTML template for rendering weather data
├── static
│   └── style.css           # Optional CSS file for styling
├── README.md               # This README file
