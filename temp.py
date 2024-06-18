import requests
from bs4 import BeautifulSoup
import urllib.request
from say import speak

def temperature(query):
    search = query
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"htal.parser") 
    temp = data.find("div",class_="BNeawe").text
    speak(f"current {search} is {temp}")

city="pune"

import pyowm
import datetime
def weather_at_place(city):
    owm=pyowm.OWM('enter your api key')
    location=owm.weather_at_place(f'{city}')
    weather=location.get_weather()
    temp=weather.get_temperature('celsius')
    humidity=weather.get_humidity()
    date=datetime.datetime.now().strftime("%A:%d:%B:%Y")
    current_temp=temp['temp']
    maximum_temp=temp['temp_max']
    min_temp=temp['temp_min']
    speak(f'The current temperature on {city} is {current_temp} degree celsius ')
    speak(f'The estimated maximum temperature for today {date} on {city} is {maximum_temp} degree celcius')
    speak(f'The estimated minimum temperature for today {date} on {city} is {min_temp} degree celcius')
    speak(f'The air is {humidity}% humid today on {city}')
            
temperature("pune")