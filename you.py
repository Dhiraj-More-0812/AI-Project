from baby import speak
import pywhatkit as kit
from pytube import YouTube
def dow():
    speak("Paste video url in terminal to download")
    url =input("paste your url")
    aa = YouTube('url').streams.first().download()
    print(aa)

def play(query):
    qaa = query.replace('play',"")
    qee = qaa.replace('on yotube',"")
    kit.playonyt(qee)
    

                

