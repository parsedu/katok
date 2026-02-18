import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLCDNumber

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Электронный индикатор")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()
        self.disp = QLCDNumber(self)
        self.disp.setDigitCount(5)

        self.button = QPushButton("Прибавить", self)
        self.button.clicked.connect(self.invalue)

        layout.addWidget(self.disp)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.val = 0
        self.updisp()

    def invalue(self):
        self.val += 1
        self.updisp()

    def updisp(self):
        self.disp.display(self.val)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
