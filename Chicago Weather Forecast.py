import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/3.0/weather?"
API_KEY = "3b87eea11e1cdb5d9a919292b0a4f8bc"
CITY = "Chicago"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

print(response)