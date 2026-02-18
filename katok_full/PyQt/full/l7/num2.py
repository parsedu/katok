import sys
from PyQt5 import QtCore, QtWidgets, QtGui


class MyEvent(QtCore.QEvent):
    idType = QtCore.QEvent.registerEventType()

    def __init__(self, data):
        super().__init__(MyEvent.idType)
        self.data = data

    def get_data(self):
        return self.data

class MyLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def customEvent(self, e):
        if e.type() == MyEvent.idType:
            self.setText("Получены данные: {0}".format(e.get_data()))


class ExampleApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.label = MyLabel("Жмякни сюда", self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setGeometry(50, 50, 200, 50)
        self.label.mousePressEvent = self.labelMousePressEvent

    def labelMousePressEvent(self, event):
        e = QtGui.QMouseEvent(
            QtCore.QEvent.MouseButtonPress,
            QtCore.QPoint(5, 5),
            QtCore.Qt.LeftButton,
            QtCore.Qt.LeftButton,
            QtCore.Qt.NoModifier
        )

        QtCore.QCoreApplication.sendEvent(self.label, MyEvent("512"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.resize(300, 200)
    window.setWindowTitle("Искусственное событие в PyQt5")
    window.show()
    sys.exit(app.exec_())
