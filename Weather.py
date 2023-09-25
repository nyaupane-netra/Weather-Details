import requests
from pprint import pprint

API_Key = 'b5ffad1b569b6b9e546430c5c4375251'

city = input("Enter a city: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid=" + API_Key+ "&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
