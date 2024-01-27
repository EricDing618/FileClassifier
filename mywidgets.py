from PyQt5.QtWidgets import QWidget,QMainWindow
from PyQt5.QtCore import Qt

def lesshint(object:QWidget|QMainWindow):
    object.setWindowFlags(Qt.WindowType.FramelessWindowHint)
    object.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
class MyWidget(QWidget):
    def __init__(self, parent=None) -> None:
        super(MyWidget,self).__init__(parent)
        
    #---gtj 实现鼠标拖拽功能
    def mousePressEvent(self, event):
        self.pressX = event.x()    #记录鼠标按下的时候的坐标
        self.pressY = event.y()

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()   #获取移动后的坐标
        moveX = x-self.pressX
        moveY = y-self.pressY  #计算移动了多少
 
        positionX = self.frameGeometry().x() + moveX
        positionY = self.frameGeometry().y() + moveY    #计算移动后主窗口在桌面的位置
        self.move(positionX, positionY)

class MyWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super(MyWindow,self).__init__(parent)
        
    #---gtj 实现鼠标拖拽功能
    def mousePressEvent(self, event):
        self.pressX = event.x()    #记录鼠标按下的时候的坐标
        self.pressY = event.y()

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()   #获取移动后的坐标
        moveX = x-self.pressX
        moveY = y-self.pressY  #计算移动了多少
 
        positionX = self.frameGeometry().x() + moveX
        positionY = self.frameGeometry().y() + moveY    #计算移动后主窗口在桌面的位置
        self.move(positionX, positionY)