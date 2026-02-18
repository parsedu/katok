import sys
from PyQt5 import QtWidgets, QtGui

class ExampleApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.lv = QtWidgets.QListView(self)
        self.sti = QtGui.QStandardItemModel(self)
        lst = ['Perl', 'PHP', 'Python', 'Ruby']
        for row in range(len(lst)):
            if row == 2:
                icon_file = 'py.png'
            else:
                icon_file = 'i.png'

            item = QtGui.QStandardItem(QtGui.QIcon(icon_file), lst[row])
            self.sti.appendRow(item)
        self.lv.setModel(self.sti)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lv)
        self.setLayout(layout)

        self.setWindowTitle("Список")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec_())
