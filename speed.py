from say import speak
import speedtest as sp
def test():
    stt = sp.Speedtest()
    di=stt.download()
    up=stt.upload()
    speak(f"sir! uploading speed is {up} and downloadimg speed is {di}")
    print(f"sir! uploading speed is {up} and downloadimg speed is {di}")

def chekserver():
    servernames =[]  
    stt = sp.Speedtest()
  
    stt.get_servers(servernames)  
  
    print(stt.results.ping)  