import tkinter

import sys
import threading

screen_main =tkinter.Tk(screenName=None, baseName=None, className='Tk', useTk=1)
screen_main.configure(background='black')
screen_main.geometry("285x323")
screen_main.minsize(285,323)
# set maximum window size value
screen_main.maxsize(285,323)
# Use overrideredirect() method
screen_main.overrideredirect(True)
screen_main.positionfrom('bottomleft')



class Redirect():
    def __init__(self,widget,autoscroll=True):
        self.autoscroll =autoscroll
        self.widget=widget
        
    def write(self,text):
        self.widget.insert('end','text')
        if self.autoscroll:
            self.widget.see('end')
            
def run():
    #threading.Thread(target=main).start()
    def flush(self):
        pass
    

def guide_task():
    print('hey! i am jarvis')
    print('i am your personal assitance')
    
def guide_run():
    threading.Thread(target=guide_task).start()
     
terminal=tkinter.Text(screen_main)
terminal.configure(background='red',foreground='white')
terminal.configure(width=40,height=20)
terminal.configure(font=('arial',10))
terminal.place(x=0,y=0)


guide_run()
old_stdout =sys.stdout
sys.stdout = Redirect(terminal)
       

screen_main.mainloop()