from say import speak
from say import takeCommand
import os


def file():
    speak("sir please tell me you want to hide this folder or make it visible for everyone")
    condition= takeCommand().lower()
    if "hide" in condition:
        os.system("attrib +h /s/d") 
        speak("sir, all the files in this folder are now hidden.")
    elif "visible" in condition:
        os.system("attrib -h /s /d")
        speak("sir, all the files in this folder are now visible to everyone. i wish you are taking")
    elif 'leave it' in condition or 'cancel' in condition:
        speak("ok sir as your wish")
        



