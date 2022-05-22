
from random import random
import PyQt6.QtWidgets as QtWidgets

import random

from stack import stack


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Data")
        self.resize(750, 450)
        self.setContentsMargins(10,20,10,20)
        main_widget = QtWidgets.QWidget(self)
        self.centralWidget = main_widget
        self.layout = QtWidgets.QGridLayout(self)
        self.centralWidget.setLayout(self.layout)

        balls = self.game_gen()

        self.stack_1 = stack(self,balls[0:4])
        self.layout.addWidget(self.stack_1,0,0,1,1)
        self.stack_2 = stack(self,balls[4:8])
        self.layout.addWidget(self.stack_2,0,1,1,1)
        self.stack_3 = stack(self,balls[8:12])
        self.layout.addWidget(self.stack_3,0,2,1,1)
        self.stack_4 = stack(self,balls[12:16])
        self.layout.addWidget(self.stack_4,0,3,1,1)
        self.stack_5 = stack(self,balls[16:20])
        self.layout.addWidget(self.stack_5,0,4,1,1)
        self.stack_6 = stack()
        self.layout.addWidget(self.stack_6,0,5,1,1)
        self.stack_7 = stack()
        self.layout.addWidget(self.stack_7,0,6,1,1)

        self.check = QtWidgets.QPushButton('Check')
        self.layout.addWidget(self.check,1,0,1,7)
        self.check.clicked.connect(self.check_game)

        self.layout.setHorizontalSpacing(10)
        self.setCentralWidget(self.centralWidget)

    def game_gen(self):
        red = ['r1', 'r2', 'r3', 'r4']
        green = ['g1', 'g2', 'g3', 'g4']
        blue = ['b1', 'b2', 'b3', 'b4']
        yellow = ['y1', 'y2', 'y3', 'y4']
        brown = ['w1', 'w2', 'w3', 'w4']
        balls = [*red, *green, *blue, *yellow, *brown]
        random.shuffle(balls)
        return balls




    def check_game(self):
        if self.check_win():
            self.check.setText('Win')
        else:
            self.check.setText('not yet check again')


    def check_win(self):

        if len(self.stack_1.tube) != 4 and len(self.stack_1.tube) != 0:
            print(1,self.stack_1.tube)
            return False
        if len(self.stack_2.tube) != 4 and len(self.stack_2.tube) != 0:
            print(2)
            return False
        if len(self.stack_3.tube) != 4 and len(self.stack_3.tube) != 0:
            print(3)
            return False
        if len(self.stack_4.tube) != 4 and len(self.stack_4.tube) != 0:
            print(4)
            return False
        if len(self.stack_5.tube) != 4 and len(self.stack_5.tube) != 0:
            print(5)
            return False
        if len(self.stack_6.tube) != 4 and len(self.stack_6.tube) != 0:
            print(6)
            return False
        if len(self.stack_7.tube) != 4 and len(self.stack_7.tube) != 0:
            print(7)
            return False

        try:s1 = all(element[0] == self.stack_1.tube[0][0] for element in self.stack_1.tube)
        except:s1 = True
        
        try:s2 = all(element[0] == self.stack_2.tube[0][0] for element in self.stack_2.tube)
        except:s2 = True

        try:s3 = all(element[0] == self.stack_3.tube[0][0] for element in self.stack_3.tube)
        except: s3 = True

        try:s4 = all(element[0] == self.stack_4.tube[0][0] for element in self.stack_4.tube)
        except:s4 = True


        try:s5 = all(element[0] == self.stack_5.tube[0][0] for element in self.stack_5.tube)
        except:s5 = True

        try:s6 = all(element[0] == self.stack_6.tube[0][0] for element in self.stack_6.tube)
        except:s6 = True

        try:s7 = all(element[0] == self.stack_7.tube[0][0] for element in self.stack_7.tube)
        except:s7 = True

        print(s1 , s2 , s3 , s4 , s5 , s6 , s7)
        if s1 and s2 and s3 and s4 and s5 and s6 and s7:
            return True
        else:
            return False

            
        
        
        
        
        
        


        