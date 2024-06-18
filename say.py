
from googletrans.models import Translated
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr 
import googletrans


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



speak('hello')
def takeCommand():
    #It takes microphone input from the user and returns string output
    if 1:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...") 
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            
            

        except Exception as e:
            # print(e)    
            print("Say that again please...")  
            return "None"
        return query

