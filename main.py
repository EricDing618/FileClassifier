# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#导入需要的库（包）
from PyQt5.QtCore import (
    Qt,
    QCoreApplication,
    QCoreApplication
)

from PyQt5.QtWidgets import (
    QApplication,
    QListWidgetItem,
    QFileDialog,
    QMessageBox
)

from tools import about,helps
from config import * #默认整理方式
from json5 import load
from os import getcwd,listdir
import os.path
from pathlib import Path
from numpy import array
from classifier import classify
from time import time
from mainui import Ui_MainWindow

def LowerAll(array_:list[str]):
    a=[]
    for i in range(len(array_)):
        a.append(array_[i].lower())
    return a
        
#UI界面
class Ui_MainWindow(Ui_MainWindow):

    #绑定功能
    def start(self):
        try:
            classifydir=self.lineEdit.text()
            timer=0
            if '/' in classifydir:
                classifydir='\\'.join(classifydir.split('/')) #防止误判
            if os.path.samefile(classifydir,getcwd()): #拦截以程序本身做实验的操作
                QMessageBox.critical(None,'错误','请不要整理程序本身的文件夹！')
            else:
                dirlist=listdir(classifydir)
                a=[]
                self.listWidget.clear()
                if dirlist != []:
                    if 'desktop.ini' in dirlist:
                        dirlist.remove('desktop.ini')
                    FILE_TOTAL_NUMBER=len(dirlist)
                    for i in range(FILE_TOTAL_NUMBER):
                        path=os.path.join(classifydir,dirlist[i])
                        '''if '/' in path:
                            path='\\'.join(path.split('/'))''' 
                        if Path(path).is_file() or Path(path).is_dir()==False:
                            a.append(path)
                            item = QListWidgetItem(None)
                            item.setText(path)
                            item.setToolTip(path)
                            self.listWidget.addItem(item)
                            self.listWidget.setCurrentRow(self.listWidget.count()-1)
                    FILE_TOTAL_NUMBER=len(a)
                    print(f'共有{FILE_TOTAL_NUMBER}个文件需整理。')
                    f=load(open('./settings.json',encoding='utf-8'))
                    dirs=array(a)
                    timer=time()
                    if f:
                        for i in f.keys():
                            f[i]=LowerAll(f[i])
                        classify(dirs,f.items(),True)
                    else:
                        classify(dirs)
        except FileNotFoundError as e:
            print(e)
            QMessageBox.critical(None,'错误',str(e).split(": ",1)[-1]+'文件已损坏或丢失！')
        except Exception as e:
            print(e)
            QMessageBox.critical(None,'错误',f'无法分类，原因：\n{str(e)}')
        else:
            if timer: #计时器正常工作
                print('Classify successfully.')
                USETIME=str(time()-timer)+'s'
                print(f'文件整理共用时间：{USETIME}')
                QMessageBox.information(None,'提示',f'成功分类{FILE_TOTAL_NUMBER}个文件，共用{USETIME}。')
        
    def choosedir(self):
        self.dir=QFileDialog.getExistingDirectory(None,'选择文件夹',getcwd())
        if self.dir:
            print('DirPath:'+self.dir)
            self.lineEdit.setText(self.dir)

    #UI代码
    def setupUi(self, win):
        super().setupUi(win)
        self.pushButton.clicked.connect(about)
        self.pushButton_2.clicked.connect(helps)
        self.choose.clicked.connect(self.choosedir)
        self.choose_2.clicked.connect(self.start)

import icon_rc
if __name__ == "__main__":
    from sys import argv,exit
    from mywidgets import MyWindow,lesshint
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(argv)
    MainWindow = MyWindow()
    lesshint(MainWindow)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    exit(app.exec_())
