# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from MyWindow import MyWindow   # Предполагается, что класс MyWindow описан в файле MyWindow.py

class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        # Встраивание существующего виджета
        self.myWidget = MyWindow()
        self.myWidget.vbox.setContentsMargins(0, 0, 0, 0)
        # Дополнительная кнопка
        self.button = QtWidgets.QPushButton("Изменить надпись")
        mainBox = QtWidgets.QVBoxLayout()
        mainBox.addWidget(self.myWidget)
        mainBox.addWidget(self.button)
        self.setLayout(mainBox)
        # Подключение слота
        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        self.myWidget.label.setText("Новая надпись")
        self.button.setDisabled(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyDialog()
    window.setWindowTitle("Преимущество ООП-стиля")
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec_())