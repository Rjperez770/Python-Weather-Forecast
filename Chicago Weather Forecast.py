import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "3b87eea11e1cdb5d9a919292b0a4f8bc"
CITY = "Chicago"
FAHRENHEIT = "imperial"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY + "&units=" + FAHRENHEIT

response = requests.get(url).json()

temp_f = response['main']['temp']
feels_like_f = response['main']['feels_like']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
wind_speed = response['wind']['speed']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"Temperature in {CITY}: {temp_f}℉")
print(f"Temperature in {CITY}: {feels_like_f}℉")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {wind_speed}m/s")
print(f"General Weather in {CITY}: {description}")
print(f"Sun Rises in {CITY} at {sunrise_time} local time")
print(f"Sun Sets in {CITY} at {sunset_time} local time")