import datetime as dt
import requests

BASE_URL="http://api.openweathermap.org/data/2.5/weather?"
API_KEY= "81e5322b66aa193f3eb4ed6fb8002d55"
CITY = "India"

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius=kelvin-2773.15
    fahreheit=celsius*(9/5)+32
    return celsius,fahreheit

url=BASE_URL + "appid=" +API_KEY + "&q=" +CITY

response = requests.get(url).json()

temp_kelvin=response['main']['temp']
temp_celsius,temp_fahrenheit=kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin=response['main']['feels_like']
feels_like_celsius,feels_like_fahrenheit=kelvin_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed=response['wind']['speed']
humidity=response['main']['humidity']
description=response['weather'][0]['description']

sunrise_time=dt.datetime.utcfromtimestamp(response['sys']['sunrise']+response['timezone'])
sunset_time=dt.datetime.utcfromtimestamp(response['sys']['sunset']+response['timezone'])

print(f"tempertature in {CITY}: {temp_celsius:2f}c or {temp_fahrenheit:.2f}F")
print(f"tempertature in {CITY} feels like: {feels_like_celsius:2f}c or {feels_like_fahrenheit:.2f}F")
print(f"Humidity in {CITY}: {humidity}%")
print(f"wind speed in {CITY}: {wind_speed}m/s")
print(f"General weather in {CITY}: {description}")
print(f"Sun rise in {CITY} at {sunrise_time} local time.")
print(f"Sun set in {CITY} at {sunset_time} local time.")

