from os import system
from threading import Thread
from PyQt5.QtWidgets import QMessageBox
def about_bind():
    if system('about.html'):
        print('About File is open.')
    else:
        QMessageBox.critical(None,'错误','无法打开关于！')
def help_bind():
    if system('help.html'):
        print('About File is open.')
    else:
        QMessageBox.critical(None,'错误','无法打开帮助！')

def about():
    a=Thread(target=about_bind)
    a.start()
def helps():
    a=Thread(target=help_bind)
    a.start()
