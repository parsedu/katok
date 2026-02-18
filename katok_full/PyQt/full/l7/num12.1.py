import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

class Browser(QtWidgets.QWidget):
    def __init__(self):
        super(Browser, self).__init__()

        self.wv = QWebEngineView(self)
        self.wv.setHtml("<h1>Заголовок</h1><a href='page2.html'>вторая страница</a>")
        self.find_button = QtWidgets.QPushButton("Найти 'Python'", self)
        self.find_button.clicked.connect(self.find_text)
        self.copy_button = QtWidgets.QPushButton("Копировать текст", self)
        self.copy_button.clicked.connect(self.copy_text)
        self.reload_button = QtWidgets.QPushButton("Перезагрузить", self)
        self.reload_button.clicked.connect(self.reload_page)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.wv)
        layout.addWidget(self.find_button)
        layout.addWidget(self.copy_button)
        layout.addWidget(self.reload_button)
        self.setLayout(layout)
        self.setWindowTitle("Веб-браузер")

    def find_text(self):
        # Передаём callback третьим аргументом (позиционно)
        self.wv.page().findText('Python', self.highlight_found_text)

    def highlight_found_text(self, result):
        if result:
            print("Текст найден!")
        else:
            print("Текст не найден.")

    def copy_text(self):
        # Внимание: document.execCommand может быть устаревшим
        self.wv.page().runJavaScript("document.execCommand('selectAll');")
        self.wv.page().runJavaScript("document.execCommand('copy');")

    def reload_page(self):
        self.wv.reload()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Browser()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())