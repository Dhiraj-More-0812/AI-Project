import datetime
import os

def alarm():
    nn =int(datetime.datetime.now().hour())
    if nn==22:
        mus = 'C:\\New folder\\SONG'
        song =os.listdir(mus)
        os.startfile(os.path.join(mus, song[0]))
