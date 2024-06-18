
import cv2
import urllib.request
import numpy as np
import time
from say import speak
import pyautogui as pg
from say import takeCommand
def open():
    cap = cv2.VideoCapture (0)
    while True:
        ret, img = cap.read()
        cv2.imshow('webcam', img)
        k = cv2.waitKey (50)
        if k==27:
            break;
    cap.release()
    cv2.destroyAllWindows()


def mobile():
    URL = "http://192.168.1.103:8080/shot.jpg"
    while True:
        img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)
        cv2.imshow('IPWebcam', img)
        q = cv2.waitKey(1)
        if q == ord("q"):
            break;
    cv2.destroyAllWindows ()
 
import os


def screenshot():
    image=pg.screenshot()
    speak("screen shot taken")
    speak("what do you want to save it as?")
    filename=takeCommand()
    image.save(filename+".png")
    speak("do you want me to show it")
    ans=takeCommand().lower()
    if "yes" in ans:
        os.startfile(filename+".png")
    else:
        speak("never mind")
   
