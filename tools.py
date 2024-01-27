from os import system
from threading import Thread
def about():
    a=Thread(target=system,args=('about.html',))
    a.start()
def helps():
    a=Thread(target=system,args=('help.html',))
    a.start()