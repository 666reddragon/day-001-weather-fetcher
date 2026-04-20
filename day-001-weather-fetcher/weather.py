"""
Day 1 - Weather Fetcher
Date: 2026-04-20
Purpose: Fetch and display current weather for any city using OpenWeatherMap API
"""

import requests

def get_weather(city_name, api_key):
    """Fetch current weather for a given city"""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,      # ← Fixed: 'q' not empty string
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]
            
            print(f"\n📍 Weather in {city_name.title()}:")
            print(f"🌡️ Temperature: {temp}°C (feels like {feels_like}°C)")
            print(f"💧 Humidity: {humidity}%")
            print(f"☁️ Condition: {description.capitalize()}")
        else:
            print(f"Error: {data.get('message', 'City not found')}")
            
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

# Usage
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Get free key from https://openweathermap.org/api
    city = input("Enter city name: ")
    get_weather(city, API_KEY)
