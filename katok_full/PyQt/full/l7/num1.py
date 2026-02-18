import PyQt5
from PyQt5 import QtCore, QtWidgets


class MyFilter(QtCore.QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

    def eventFilter(self, obj, e):
        if e.type() == QtCore.QEvent.KeyPress:

            if e.key() in (QtCore.Qt.Key_A, QtCore.Qt.Key_E, QtCore.Qt.Key_Y,
                           QtCore.Qt.Key_U,QtCore.Qt.Key_I,QtCore.Qt.Key_O):
                print(f'Событие от клавиши <{e.text().upper()}> не дойдет до компонента')
                return True
        return super().eventFilter(obj, e)


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.text_edit = QtWidgets.QTextEdit(self)
        self.text_edit.setPlaceholderText("Гласные буквы не будут вводиться")
        self.setCentralWidget(self.text_edit)
        self.filter = MyFilter(self)
        self.text_edit.installEventFilter(self.filter)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.resize(250, 100)
    window.show()
    sys.exit(app.exec_())
