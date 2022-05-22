import PyQt6.QtWidgets as QtWidgets
from PyQt6.QtWidgets import  QPushButton
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDrag, QPixmap



class stack(QtWidgets.QGroupBox):
    def __init__(self, parent=None, balls:list=[]):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.tube = []
        self.first_time = False
        for ball in balls:
            self.tube.append(ball)
        #background-color: yellow;
        self.setStyleSheet('''
        QGroupBox {
             border : 2px solid black;
             border-radius: 10px;
             }
        ''')

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)
        self.layout.addStretch(1)

        self.ui()

    def clearLayout(self,layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    self.clearLayout(child.layout())
        self.layout.addStretch(1)
    
    def ui(self):
        self.clearLayout(self.layout)
        print(self.tube)
        for item in reversed(self.tube):        
            self.btn = Button(self, item)
            self.layout.addWidget(self.btn)
            self.btn.setMinimumSize(40, 40)
            

    def dragEnterEvent(self, e):
        print(e.source().objectName())
        if len(self.tube) < 4 and e.source().objectName() == e.source().parent().tube[-1]:
            try:
                if e.source().objectName()[0] == self.tube[-1][0]:
                    e.accept()
            except:
                e.accept()
            


    def dropEvent(self, e):
        print('drop >> ', self.tube)
        print(e.source().parent().tube.pop())
        self.tube.append(e.source().objectName())
        self.ui()
        e.source().parent().ui()
        e.accept()




class Button(QPushButton):
    def __init__(self, parent, color):
        super().__init__(parent)
        self.setObjectName(color)
        if color[0] == 'r':
            self.setStyleSheet("QPushButton{background-color: red;}")
        elif color[0] == 'b':
            self.setStyleSheet("QPushButton{background-color: blue;}")
        elif color[0] == 'g':
            self.setStyleSheet("QPushButton{background-color: green;}")
        elif color[0] == 'y':
            self.setStyleSheet("QPushButton{background-color: yellow;}")
        elif color[0] == 'w':
            self.setStyleSheet("QPushButton{background-color: brown;}")
        

    def mouseMoveEvent(self, e):
        mimeData = QMimeData()
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        pixmap = QPixmap(self.size())
        self.render(pixmap)
        drag.setPixmap(pixmap)
        dropAction = drag.exec(Qt.DropAction.MoveAction)






# class stack:
#     def __init__(self,data:list) -> None:
#         self.data = data

#     def pop(self):
#         return self.data.pop()

#     def push(self,d):
#         self.data.append(d)

#     def top(self):
#         return self.data[-1]


        
        

        






