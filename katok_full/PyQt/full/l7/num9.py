from PyQt5 import QtWidgets, QtCore
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
splintter = QtWidgets.QSplitter(QtCore.Qt.Vertical)
label1 = QtWidgets.QLabel("Содержимое компонента 1")
label2 = QtWidgets.QLabel("Содержимое компонента 2")
label1.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Plain)
label2.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Plain)

splintter.addWidget(label1)
splintter.addWidget(label2)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(splintter)
window.setLayout(vbox)
window.show()
sys.exit(app.exec_())