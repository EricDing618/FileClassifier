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
    QRect,
    QCoreApplication,
    QMetaObject,
    QCoreApplication
)

from PyQt5.QtWidgets import (
    QPushButton,
    QLabel,
    QLineEdit,
    QApplication,
    QWidget,
    QListWidget,
    QSizePolicy,
    QListView,
    QListWidgetItem,
    QFileDialog,
    QMessageBox,
)

from PyQt5.QtGui import (
    QFont,
    QIcon,
    QPixmap
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
        
#UI界面
class Ui_MainWindow(object):

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
                    for i in range(len(dirlist)):
                        path=os.path.join(classifydir,dirlist[i])
                        '''if '/' in path:
                            path='\\'.join(path.split('/'))''' 
                        print(path)
                        if Path(path).is_file() or Path(path).is_dir()==False:
                            a.append(path)
                            item = QListWidgetItem(None)
                            item.setText(path)
                            item.setToolTip(path)
                            self.listWidget.addItem(item)
                            self.listWidget.setCurrentRow(self.listWidget.count()-1)
                    f=load(open('./settings.json',encoding='utf-8'))
                    dirs=array(a)
                    timer=time()
                    if f:
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
                print('文件整理共用时间：'+str(time()-timer)+'s')
                QMessageBox.information(None,'提示','分类成功！')
        
    def choosedir(self):
        self.dir=QFileDialog.getExistingDirectory(None,'选择文件夹',getcwd())
        if self.dir:
            print('DirPath:'+self.dir)
            self.lineEdit.setText(self.dir)

    #UI代码
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 430)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icon/icon.png"), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00568182 rgba(0, 100, 255, 255), stop:0.994318 rgba(255, 0, 171, 255));\n"
"border-top-left-radius:20px;\n"
"border-top-right-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QRect(150, 207, 271, 192))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setStyleSheet("background-color:grey;\n"
"color:white;\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius:5px;\n")
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setFlow(QListView.TopToBottom)
        self.listWidget.setItemAlignment(Qt.AlignBaseline|Qt.AlignCenter|Qt.AlignHCenter|Qt.AlignJustify|Qt.AlignTop|Qt.AlignVCenter)
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(QRect(90, 120, 141, 36))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:None;\n"
"color:white;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QRect(220, 128, 151, 22))
        font = QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        #self.lineEdit.setReadOnly(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:None;\n"
"border-radius:10px;")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.choose = QPushButton(self.centralwidget)
        self.choose.setGeometry(QRect(380, 126, 75, 27))
        font = QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.choose.setFont(font)
        self.choose.clicked.connect(self.choosedir)
        self.choose.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 85, 255);\n"
"    border-radius:9px;\n"
"    border-width:4px;\n"
"    color:white;\n"
"    border-color:rgba(255,255,255,30);\n"
"}\n"
"")
        self.choose.setObjectName("choose")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(-10, 400, 75, 23))
        font = QFont()
        font.setFamily("Microsoft YaHei")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:None;\n"
"color:white;"
)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(about)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setGeometry(QRect(240, 400, 54, 21))
        font = QFont()
        font.setFamily("Microsoft YaHei")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:None;\n"
"color:white;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QRect(484, 400, 51, 23))
        font = QFont()
        font.setFamily("Microsoft YaHei")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:None;\n"
"color:white;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(helps)
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(180, 50, 221, 36))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(23)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:None;\n"
"color:white;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.close = QPushButton(self.centralwidget)
        self.close.setGeometry(QRect(490, 10, 41, 31))
        font = QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.close.setFont(font)
        self.close.setStyleSheet("background-color:None;\n"
"color:white;")
        self.close.setObjectName("close")
        self.choose_2 = QPushButton(self.centralwidget)
        self.choose_2.setGeometry(QRect(246, 162, 81, 31))
        font = QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.choose_2.setFont(font)
        self.choose_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 85, 255);\n"
"    border-radius:12px;\n"
"    border-width:4px;\n"
"    color:white;\n"
"    border-color:rgba(255,255,255,30);\n"
"}\n"
"")
        self.choose_2.setObjectName("choose_2")
        self.choose_2.clicked.connect(self.start)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.close.clicked.connect(MainWindow.close)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FileClassifier"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "文件夹路径："))
        self.choose.setText(_translate("MainWindow", "选择"))
        self.pushButton.setText(_translate("MainWindow", "关于"))
        self.label_3.setText(_translate("MainWindow", "v1.1"))
        self.pushButton_2.setText(_translate("MainWindow", "帮助"))
        self.label.setText(_translate("MainWindow", "FileClassifier"))
        self.close.setText(_translate("MainWindow", "×"))
        self.choose_2.setText(_translate("MainWindow", "开始"))

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
