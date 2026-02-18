from PyQt5 import QtWidgets
import sys

def on_clicked():
    print("Кнопка нажата. Функация on_clicked()")

class MyClass():
    def __init__(self, x=0):
        self.x = x

    def __call__(self):
        print("Кнопка нажата. Метод MyClass.__call()")
        print("x=", self.x)

    def on_ckicked(self):
        print("Кнопка нажата. Метод MyClass.on_clicked()")


obj = MyClass()
app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton("Нажми меня")
button.clicked.connect(on_clicked)
button.clicked.connect(obj.on_ckicked)
button.clicked.connect(MyClass(10))
button.clicked.connect(lambda : MyClass(5))
button.show()
sys.exit(app.exec_())