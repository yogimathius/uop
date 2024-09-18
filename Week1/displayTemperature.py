import requests
import os
from datetime import date
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv('WEATHER_API_KEY')

base_url = "http://api.openweathermap.org/data/2.5/weather?"


def displayTemperature(city_name):
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name


    response = requests.get(complete_url)
    today = date.today()

    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        current_temperature_kelvin = y["temp"]
        current_temperature_celsius = current_temperature_kelvin - 273.15

        print(f"Temperature (in kelvin unit) = {current_temperature_kelvin:.2f}\n"
              f"Temperature (in celsius unit) = {current_temperature_celsius:.2f}\n"
              f"Date: {today}")
    else:
        print("City Not Found")

# ref: https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/

displayTemperature("Squamish")