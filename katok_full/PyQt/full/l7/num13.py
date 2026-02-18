import sys
from PyQt5 import QtWidgets, QtCore


class ExampleApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.slm = QtCore.QStringListModel(self)
        self.slm.insertRows(0, 4)
        self.slm.setData(self.slm.index(0), 'Perl')
        self.slm.setData(self.slm.index(1), 'PHP')
        self.slm.setData(self.slm.index(2), 'Python')
        self.slm.setData(self.slm.index(3), 'Ruby')

        self.combo_box = QtWidgets.QComboBox(self)
        self.combo_box.setModel(self.slm)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.combo_box)
        self.setLayout(layout)
        self.setWindowTitle("Список")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec_())
