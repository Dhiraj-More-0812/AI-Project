
import psutil
from say import speak

def per():
    battery = psutil.sensors_battery()
    percentage = battery.percent
    speak(f"sir our system have {percentage} percent battery")
    if percentage>=75:
        speak("we have enough power to continue our work")
    elif percentage>=40 and percentage<=75:
        speak("we should connect our system to charging point to charge our battery")
    elif percentage>=15 and percentage<=38:
        speak("we don't have enough power to work, please connect to charging")
    elif percentage<=15:
        speak("we have very low power, please connect to charging the system will shutdown very soon")     
  

def feel():
    battery = psutil.sensors_battery()
    percentage = battery.percent
    speak(f"sir our system have {percentage} percent battery")
    if percentage>=75:
        speak("sir! i am fully charge  and loaded , waiting for your command")
    elif percentage>=40 and percentage<=75:
        speak("sir! i am fine and ready in am chare 40%")
    elif percentage>=15 and percentage<=38:
        speak("sir! i will be offline with in some minutes ,if you don't plug in charge....")
    elif percentage<=15:
        speak("sir!  very  low power of our bettery , please connect to charging the system will shutdown and me also")

