from PyQt5 import QtCore, QtGui, QtWidgets


class MyEvent(QtCore.QEvent):
    idType = QtCore.QEvent.registerEventType()
    def __init__(self, data):
        super().__init__(MyEvent.idType)
        self.data = data
    def get_data(self):
        return self.data


class CustomLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def customEvent(self, e):
        if e.type() == MyEvent.idType:
            self.setText(f"Получены данные:{0}".format(e.get_data()))


app = QtWidgets.QApplication([])
label = CustomLabel("Начальный текст")
label.resize(300, 100)
label.show()



e = QtGui.QMouseEvent(
    QtCore.QEvent.MouseButtonPress,
    QtCore.QPoint(5, 5),
    QtCore.Qt.LeftButton,
    QtCore.Qt.LeftButton,
    QtCore.Qt.NoModifier,
)
QtCore.QCoreApplication.postEvent(label,  e)


QtCore.QCoreApplication.postEvent(label,  MyEvent("512"))

app.exec_()
