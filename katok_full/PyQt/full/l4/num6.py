import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget
import time
import os

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.elapsed_time = 0
        self.elapsed_time2 = 0
        self.timer_id = None
        font = QFont('Areal', 14)

        #self.setAttribute(Qt.WA_TranslucentBackground)
        #self.setGeometry(100, 100, 400, 400)
        #self.setWindowFlags(Qt.FramelessWindowHint)

        self.label = QtWidgets.QLabel("00:00:00", self)
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.label.move(150, 100)
        self.label.resize(100, 30)
        self.label.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
        self.label.setFont(font)

        self.label2 = QtWidgets.QLabel("00:00:00", self)
        self.label2.setAlignment(QtCore.Qt.AlignHCenter)
        self.label2.move(150, 150)
        self.label2.resize(100, 30)
        self.label2.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
        self.label2.setFont(font)

        self.button1 = QtWidgets.QPushButton("Запустить", self)
        self.button1.setFixedSize(200, 30)
        self.button1.move(100, 250)
        self.button1.setCheckable(True)
        """
        self.button2 = QtWidgets.QPushButton("Пауза", self)
        self.button2.setFixedSize(100, 30)
        self.button2.move(200, 250)
        self.button2.setEnabled(False)
        """
        self.button3 = QtWidgets.QPushButton("Выход", self)
        self.button3.setFixedSize(100, 30)
        self.button3.move(200, 300)
        self.button3.clicked.connect(self.close)

        self.button4 = QtWidgets.QPushButton("Сброс", self)
        self.button4.setFixedSize(100,30)
        self.button4.move(100,300)

        self.button1.clicked.connect(self.on_clicked_button1)
        #self.button2.clicked.connect(self.on_clicked_button2)
        self.button4.clicked.connect(self.on_clicked_button4)


    def on_clicked_button1(self):
        if self.timer_id is None:
            self.timer_id = self.startTimer(1000)
            self.button1.setText("Пауза")
        else:
            self.killTimer(self.timer_id)
            self.timer_id = None
            self.button1.setText("Старт")




    def on_clicked_button4(self):
        if self.timer_id:
            self.killTimer(self.timer_id)
            self.timer_id = None
        self.elapsed_time = 0
        self.label.setText("00:00:00")
        self.button1.setEnabled(True)

    def timerEvent(self, event):
        self.elapsed_time += 1
        h = self.elapsed_time // 3600
        m = (self.elapsed_time % 3600) // 60
        s = self.elapsed_time % 60
        time_string = f"{h:02}:{m:02}:{s:02}"
        self.label.setText(time_string)

        self.elapsed_time2 += 1
        h2 = self.elapsed_time2 // 3600
        m2 = (self.elapsed_time2 % 3600) // 60
        s2 = self.elapsed_time2 % 60
        time_string2 = f"{h2:02}:{m2:02}:{s2:02}"
        self.label2.setText(time_string2)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
