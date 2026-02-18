from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QGroupBox")
window.resize(200,80)
mainbox = QtWidgets.QVBoxLayout()
radio1 = QtWidgets.QRadioButton("&Да")
radio2 = QtWidgets.QRadioButton("&Нет")

box = QtWidgets.QGroupBox("&Вы знаете язык Python?")
hbox = QtWidgets.QHBoxLayout()
hbox.addWidget(radio1)
hbox.addWidget(radio2)
box.setLayout(hbox)
mainbox.addWidget(box)
window.setLayout(mainbox)
radio1.setChecked(True)
window.show()
sys.exit(app.exec_())

