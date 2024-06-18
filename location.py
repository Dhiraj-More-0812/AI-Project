import requests
from say import speak
import urllib.request

def find():
    try:
        ipAdd = requests.get('https://api.ipify.org').text
        print(ipAdd)
        url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
        geo_requests = requests.get(url)
    #print(geo_requests)
        geo_data = geo_requests.json()              #change scrip with ex; print(geo_data['city']) as city name ....
    # print(geo_data)
        speak("sir i am not sure, but i think we are in city ")
        print(geo_data['city'])
        speak(geo_data['city'])
        speak("of state ")
        print(geo_data['state'])
        speak(geo_data['state'])
        speak("of country")
        print(geo_data['country'])
        speak(geo_data['country'])
       
    except Exception as e:
        speak("sorry sir, Due to network issue i am not able to find where we are.") 
        pass
    
