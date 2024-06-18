import requests
# paste your api key here
api_key = "PASTE_YOUR_API_KEY"
# getting city name from user
city = input("Enter city name: ")
"""
we appending the city variable and api_key variable to complete the url. for example city name is Mumbai  then url looks like 
https://api.openweathermap.org/data/2.5/weather?q=Mumbai&units=metric&APPID=4256b3de394a56a86ee35e43af6f5c2e
"""
data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={'9d851bcb68ce0768179cb580661bd3b3'}"
)
# uncomment the following line and run it so you can get the data in json format
# print(data.json())
# getting the data
print(f"Location: {data.json().get('name')}, {data.json().get('sys').get('country')}")
print(f"Temperature: {data.json().get('main')['temp']}°C")
print(f"Weather: {data.json().get('weather')[0].get('main')}")
print(
    f"Min/Max Temperature: {data.json().get('main')['temp_min']}°C/{data.json().get('main')['temp_max']}°C"
)
print(f"Humidity: {data.json().get('main')['humidity']}%")
print(f"Wind: {data.json().get('wind')['speed']} km/h")