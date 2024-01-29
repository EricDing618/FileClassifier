from PyQt5.QtWidgets import QMessageBox
from webbrowser import open_new_tab
from pathlib import Path
from os import getcwd

def about():
    if Path(getcwd()+'\\about.html').is_file():
        open_new_tab('about.html')
        print('About File is open.')
    else:
        QMessageBox.critical(None,'错误','无法打开关于！')


def helps():
    if Path(getcwd()+'\\help.html').is_file():
        open_new_tab('help.html')
        print('Help File is open.')
    else:
        QMessageBox.critical(None,'错误','无法打开帮助！')