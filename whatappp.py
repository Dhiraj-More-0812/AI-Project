from baby import takeCommand
import pywhatkit as kit
from say import speak
import time
from say import takeCommand
import datetime

def send():
    speak("to whome you will like to dend meaasge")
    query =takeCommand().lower()
    if 'dad'in query:
        contact=98507265454
    elif "mom" in query:
        contact=9657070449
    speak("what message you would like to sey")
    msg = takeCommand().lower()
    now = datetime.now()
    ch = datetime.now().hour
    cm = datetime.now().minute
    cmm=int(cm + 2)
    kit.sendwhatmsg(contact, "msg", ch, cmm)


#def mss():
#    now = datetime.now()
#    ch = datetime.now().hour
#    cm = datetime.now().minute
#    cmm=int(cm + 2)
#    kit.sendwhatmsg(9850725456, "hi hi hi ", ch, cmm)
#
#mss()
