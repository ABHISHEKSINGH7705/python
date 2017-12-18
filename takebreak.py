import webbrowser
import time

t=3
b=0
print("this program started on"+time.ctime())
while(b<t):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=vtxa_lAaJeM")
    b=b+1
