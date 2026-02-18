from PyQt5 import QtCore, QtGui, QtWidgets
import time

class MyWindow(QtWidgets.QPushButton):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setText("Закрыть окно")
        self.clicked.connect(QtWidgets.qApp.quit)

    def load_data(self, sp):
        for i in range(1, 11):
            time.sleep(2)
            sp.showMessage("Загрузка данных... ({}%)".format(i * 10),
                           QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.black)
            QtWidgets.qApp.processEvents()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("C://Users//Admin//Desktop//1.jpg"))
    splash.showMessage("Загрузка данных... 0%",
                       QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.black)
    splash.show()
    QtWidgets.qApp.processEvents()
    window = MyWindow()
    window.setWindowTitle("Использование класса QSplashScreen")
    window.resize(300, 30)
    window.load_data(splash)
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())
