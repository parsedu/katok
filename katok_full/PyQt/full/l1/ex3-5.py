import sys
import time
from PyQt5 import QtCore, QtWidgets

import threading

from PyQt5.QtCore import QMetaObject, Qt, Q_ARG, QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QTabWidget, QWidget, QLabel, QHBoxLayout, QPushButton, QTextEdit, \
    QApplication, QProgressBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Лабораторная работа №1 - PyQt5")
        self.setGeometry(100, 100, 800, 600)


        central_widget = QWidget()
        self.setCentralWidget(central_widget)


        main_layout = QVBoxLayout(central_widget)


        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)


        self.create_task1_tab()
        self.create_task2_tab()

        self.show()

    def create_task1_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        label = QLabel("Задание 3: Управление выводом в консоль")
        label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(label)


        self.running = False
        self.paused = False


        btn_layout = QHBoxLayout()

        self.start_btn = QPushButton("Начать вывод (Ctrl+S)")
        self.start_btn.setShortcut("Ctrl+S")
        self.start_btn.clicked.connect(self.start_output)

        self.pause_btn = QPushButton("Пауза (Ctrl+P)")
        self.pause_btn.setShortcut("Ctrl+P")
        self.pause_btn.clicked.connect(self.pause_output)
        self.pause_btn.setEnabled(False)

        self.stop_btn = QPushButton("Стоп (Ctrl+T)")
        self.stop_btn.setShortcut("Ctrl+T")
        self.stop_btn.clicked.connect(self.stop_output)
        self.stop_btn.setEnabled(False)

        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.pause_btn)
        btn_layout.addWidget(self.stop_btn)

        layout.addLayout(btn_layout)

        self.console_output = QTextEdit()
        self.console_output.setReadOnly(True)
        self.console_output.setMaximumHeight(200)
        layout.addWidget(QLabel("Лог вывода:"))
        layout.addWidget(self.console_output)


        self.output_thread = None

        self.tab_widget.addTab(tab, "Задание 3")

    def start_output(self):
        if not self.running:
            self.running = True
            self.paused = False
            self.start_btn.setEnabled(False)
            self.pause_btn.setEnabled(True)
            self.stop_btn.setEnabled(True)


            self.output_thread = threading.Thread(target=self.output_worker, daemon=True)
            self.output_thread.start()

    def pause_output(self):
        self.paused = not self.paused
        if self.paused:
            self.pause_btn.setText("Продолжить (Ctrl+P)")
        else:
            self.pause_btn.setText("Пауза (Ctrl+P)")

    def stop_output(self):
        self.running = False
        self.start_btn.setEnabled(True)
        self.pause_btn.setEnabled(False)
        self.stop_btn.setEnabled(False)
        self.pause_btn.setText("Пауза (Ctrl+P)")

    def output_worker(self):
        while self.running:
            if not self.paused:

                print("*", end='', flush=True)
                QMetaObject.invokeMethod(self.console_output, "append",
                                         Qt.ConnectionType.QueuedConnection,
                                         Q_ARG(str, "*"))
                time.sleep(0.1)
            else:
                time.sleep(0.1)

    # 4-5. Длительная операция с разбиением
    def create_task2_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        label = QLabel("Задания 4-5: Длительная операция с прогрессом")
        label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(label)


        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)


        btn_layout = QHBoxLayout()

        self.long_op_btn = QPushButton("Запустить длительную операцию")
        self.long_op_btn.clicked.connect(self.start_long_operation)

        self.chunk_op_btn = QPushButton("Запустить разбитую операцию")
        self.chunk_op_btn.clicked.connect(self.start_chunked_operation)

        btn_layout.addWidget(self.long_op_btn)
        btn_layout.addWidget(self.chunk_op_btn)
        layout.addLayout(btn_layout)

        # Статус
        self.status_label = QLabel("Готово")
        layout.addWidget(self.status_label)

        self.tab_widget.addTab(tab, "Задания 4-5")

    def start_long_operation(self):
        self.long_op_btn.setEnabled(False)
        self.status_label.setText("Выполняется длительная операция...")
        self.progress_bar.setValue(0)


        for i in range(101):
            time.sleep(0.05)
            self.progress_bar.setValue(i)
            QApplication.processEvents()

        self.status_label.setText("Длительная операция завершена!")
        self.long_op_btn.setEnabled(True)

    def start_chunked_operation(self):
        self.chunk_op_btn.setEnabled(False)
        self.status_label.setText("Выполняется разбитая операция...")
        self.progress_bar.setValue(0)


        for chunk in range(10):
            for i in range(10):
                time.sleep(0.01)
            self.progress_bar.setValue((chunk + 1) * 10)
            QApplication.processEvents()

        self.status_label.setText("Разбитая операция завершена!")
        self.chunk_op_btn.setEnabled(True)

    # 6-8. Работа с потоками
    def create_task3_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        label = QLabel("Задания 6-8: Работа с потоками и сигналами")
        label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(label)


        self.worker_thread = WorkerThread()


        self.thread_start_btn = QPushButton("Запустить поток")
        self.thread_start_btn.clicked.connect(self.start_worker_thread)

        self.thread_stop_btn = QPushButton("Остановить поток")
        self.thread_stop_btn.clicked.connect(self.stop_worker_thread)
        self.thread_stop_btn.setEnabled(False)

        layout.addWidget(self.thread_start_btn)
        layout.addWidget(self.thread_stop_btn)


        self.thread_output = QTextEdit()
        self.thread_output.setReadOnly(True)
        layout.addWidget(QLabel("Данные из потока:"))
        layout.addWidget(self.thread_output)


        self.thread_progress = QProgressBar()
        layout.addWidget(self.thread_progress)


        self.thread_status = QLabel("Поток не запущен")
        layout.addWidget(self.thread_status)


        self.worker_thread.progress_update.connect(self.update_thread_progress)
        self.worker_thread.data_ready.connect(self.update_thread_output)
        self.worker_thread.status_update.connect(self.update_thread_status)

        self.tab_widget.addTab(tab, "Задания 6-8")

    def start_worker_thread(self):
        if not self.worker_thread.isRunning():
            self.worker_thread.start()
            self.thread_start_btn.setEnabled(False)
            self.thread_stop_btn.setEnabled(True)
            self.thread_status.setText("Поток запущен")

    def stop_worker_thread(self):
        if self.worker_thread.isRunning():
            self.worker_thread.stop()
            self.thread_start_btn.setEnabled(True)
            self.thread_stop_btn.setEnabled(False)
            self.thread_status.setText("Поток остановлен")

    def update_thread_progress(self, value):
        self.thread_progress.setValue(value)

    def update_thread_output(self, data):
        self.thread_output.append(f"Поток: {data}")

    def update_thread_status(self, status):
        self.thread_status.setText(f"Статус: {status}")


# 6-8. Класс рабочего потока с сигналами
class WorkerThread(QThread):
    progress_update = pyqtSignal(int)
    data_ready = pyqtSignal(str)
    status_update = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._is_running = True

    def run(self):
        self.status_update.emit("Поток начал работу")

        for i in range(101):
            if not self._is_running:
                break


            time.sleep(0.05)


            self.progress_update.emit(i)


            if i % 10 == 0:
                self.data_ready.emit(f"Шаг {i} выполнен")

        self.status_update.emit("Поток завершил работу")

    def stop(self):
        self._is_running = False
        self.status_update.emit("Остановка потока...")


class CustomButton(QPushButton):
    """Кастомная кнопка с повторно используемыми настройками"""

    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setMinimumSize(100, 40)
        self.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
            QPushButton:disabled {
                background-color: #cccccc;
            }
        """)


def main():
    app = QApplication(sys.argv)

    app.setStyle("Fusion")
    window = MainWindow()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()