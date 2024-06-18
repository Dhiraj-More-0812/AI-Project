from say import speak
from pywikihow import search_wikihow
import wikipedia

def to(query):  
    how = query.replace("how to","")
    max_results = 1
    how_to = search_wikihow(how, max_results)
    assert len(how_to) == 1
    how_to[0].print()
    speak(how_to[0].summary)



def who(query):
    #query = query.replace("who is", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to my data")
    print(results)
    speak(results)

def what(query):
    if'what is your name' in query:
        speak("hello sir, my name is jarvis")
    else:    
        results = wikipedia.summary(query, sentences=2)
        
        speak("According to my data")
        
        print(results)
        
        speak(results)