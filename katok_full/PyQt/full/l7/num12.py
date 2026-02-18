import sys
from PyQt5 import QtWidgets, QtCore, QtGui, QtWebEngineWidgets

class BrowserWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Простой браузер")
        self.resize(900, 600)

        # Создаём веб-вью
        self.webview = QtWebEngineWidgets.QWebEngineView()
        self.webview.setUrl(QtCore.QUrl("http://www.example.com"))
        self.setCentralWidget(self.webview)

        # Подключаем сигналы
        self.webview.titleChanged.connect(self.update_title)
        self.webview.urlChanged.connect(self.update_urlbar)
        self.webview.loadProgress.connect(self.update_progress)
        self.webview.loadFinished.connect(self.load_finished)

        # Создаём панель инструментов
        self.create_toolbar()

        # Строка состояния
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Готово")
        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setMaximumWidth(100)
        self.progress_bar.setVisible(False)
        self.status_bar.addPermanentWidget(self.progress_bar)

    def create_toolbar(self):
        toolbar = self.addToolBar("Навигация")

        # Кнопка "Назад"
        back_btn = QtWidgets.QAction("◀", self)
        back_btn.setToolTip("Назад")
        back_btn.triggered.connect(self.webview.back)
        toolbar.addAction(back_btn)

        # Кнопка "Вперёд"
        forward_btn = QtWidgets.QAction("▶", self)
        forward_btn.setToolTip("Вперёд")
        forward_btn.triggered.connect(self.webview.forward)
        toolbar.addAction(forward_btn)

        # Кнопка "Обновить"
        reload_btn = QtWidgets.QAction("⟲", self)
        reload_btn.setToolTip("Обновить")
        reload_btn.triggered.connect(self.webview.reload)
        toolbar.addAction(reload_btn)

        # Кнопка "Стоп"
        stop_btn = QtWidgets.QAction("✕", self)
        stop_btn.setToolTip("Остановить загрузку")
        stop_btn.triggered.connect(self.webview.stop)
        toolbar.addAction(stop_btn)

        # Кнопка "Домой"
        home_btn = QtWidgets.QAction("⌂", self)
        home_btn.setToolTip("Домашняя страница")
        home_btn.triggered.connect(self.go_home)
        toolbar.addAction(home_btn)

        # Адресная строка
        self.address_bar = QtWidgets.QLineEdit()
        self.address_bar.setPlaceholderText("Введите адрес...")
        self.address_bar.returnPressed.connect(self.load_url)
        toolbar.addWidget(self.address_bar)

    def load_url(self):
        url = self.address_bar.text().strip()
        if not url:
            return
        # Добавляем схему, если её нет
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        self.webview.setUrl(QtCore.QUrl(url))

    def go_home(self):
        self.webview.setUrl(QtCore.QUrl("http://www.google.com"))

    def update_title(self, title):
        self.setWindowTitle(f"{title} - Простой браузер")

    def update_urlbar(self, url):
        self.address_bar.setText(url.toString())
        self.address_bar.setCursorPosition(0)

    def update_progress(self, progress):
        if progress < 100:
            self.progress_bar.setVisible(True)
            self.progress_bar.setValue(progress)
            self.status_bar.showMessage(f"Загрузка... {progress}%")
        else:
            self.progress_bar.setVisible(False)
            self.status_bar.showMessage("Готово")

    def load_finished(self, ok):
        if not ok:
            self.status_bar.showMessage("Ошибка загрузки страницы")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec_())