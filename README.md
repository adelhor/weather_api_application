# Weather Information Retrieval System

This repository hosts a Python-based system designed to fetch and display weather information. It integrates external API services to retrieve current weather data for any specified city, offering insights into temperature, pressure, and humidity levels alongside user-friendly emoji representations.

## Features

- Retrieves current weather information including temperature, pressure, and humidity based on the user's city input.
- Translates weather conditions into Polish using the `translate` library.
- Provides emoji-based visual representation for temperature, pressure, and humidity.
- Generates an Excel report summarizing the weather data for the city with a timestamp.

### Prerequisites

Ensure you have Python installed on your system. This project requires Python 3.6 or later. In this project, Python 3.12 was specifically used within the PyCharm 2023.3.3 environment. Additionally, you need to have `pip` available to install dependencies.

### Installation
1. Clone this repository to your local machine.
```bash
git clone https://github.com/adelhor/weather-api_application.git
cd weather-api_application
```
   
2. Install the necessary Python packages:
```bash
pip install requests unidecode translate pandas python-dotenv
```

### Configuration
1. Obtain an API key from WeatherAPI.com.
2. Create a .env file in the project root and add your API key:
```bash
API_KEY=your_api_key
```
3. Make sure .env is listed in your .gitignore file to prevent exposing your API key:
```bash
# Environment variables
.env
```

### Usage
Run the main script from the terminal:

```bash
python API.py
```
Follow the interactive prompts to input a city name and choose the data you wish to view.

### Output
The program displays the selected weather information in the terminal in English and generates an Excel file "dane_pogoda_{city}_{date}.xlsx" containing the detailed data in Polish.
