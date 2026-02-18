import sys
import time
from PyQt5 import QtCore, QtWidgets

import threading

from PyQt5.QtCore import QMetaObject, Qt, Q_ARG, QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QTabWidget, QWidget, QLabel, QHBoxLayout, QPushButton, QTextEdit, \
    QApplication, QProgressBar


# 1. Класс для ООП-стиля GUI
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

        self.create_task3_tab()

        self.show()

    def create_task1_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        label = QLabel("Задание 3: Управление выводом в консоль")
        label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(label)

        # Переменные для управления потоком
        self.running = False
        self.paused = False
        self.output_thread = None

        # Кнопки
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

        # Лог вывода
        self.console_output = QTextEdit()
        self.console_output.setReadOnly(True)
        self.console_output.setMaximumHeight(200)
        layout.addWidget(QLabel("Лог вывода:"))
        layout.addWidget(self.console_output)

        self.tab_widget.addTab(tab, "Задание 3")

    def start_output(self):
        if not self.running:
            self.running = True
            self.paused = False
            self.start_btn.setEnabled(False)
            self.pause_btn.setEnabled(True)
            self.stop_btn.setEnabled(True)

            # Создаем новый поток
            self.output_thread = OutputThread()
            self.output_thread.output_signal.connect(self.update_console)
            self.output_thread.finished.connect(self.on_output_thread_finished)
            self.output_thread.start()

    def pause_output(self):
        self.paused = not self.paused
        if self.paused:
            self.output_thread.pause()
            self.pause_btn.setText("Продолжить (Ctrl+P)")
        else:
            self.output_thread.resume()
            self.pause_btn.setText("Пауза (Ctrl+P)")

    def stop_output(self):
        if self.output_thread and self.output_thread.isRunning():
            self.output_thread.stop()

    def update_console(self, char):
        self.console_output.insertPlainText(char)
        # Прокрутка вниз
        scrollbar = self.console_output.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def on_output_thread_finished(self):
        self.running = False
        self.start_btn.setEnabled(True)
        self.pause_btn.setEnabled(False)
        self.stop_btn.setEnabled(False)
        self.pause_btn.setText("Пауза (Ctrl+P)")
        self.output_thread = None

    # 4-5. Длительная операция с разбиением
    def create_task2_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        label = QLabel("Задания 4-5: Длительная операция с прогрессом")
        label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(label)

        # Прогресс бар
        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        # Кнопки для управления
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

        # Имитация длительной операции в отдельном потоке
        self.long_op_thread = LongOperationThread("long")
        self.long_op_thread.progress_signal.connect(self.update_progress)
        self.long_op_thread.finished.connect(self.on_long_op_finished)
        self.long_op_thread.start()

    def start_chunked_operation(self):
        self.chunk_op_btn.setEnabled(False)
        self.status_label.setText("Выполняется разбитая операция...")
        self.progress_bar.setValue(0)

        # Имитация разбитой операции в отдельном потоке
        self.chunk_op_thread = LongOperationThread("chunked")
        self.chunk_op_thread.progress_signal.connect(self.update_progress)
        self.chunk_op_thread.finished.connect(self.on_chunk_op_finished)
        self.chunk_op_thread.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def on_long_op_finished(self):
        self.status_label.setText("Длительная операция завершена!")
        self.long_op_btn.setEnabled(True)

    def on_chunk_op_finished(self):
        self.status_label.setText("Разбитая операция завершена!")
        self.chunk_op_btn.setEnabled(True)

    # 6-8. Работа с потоками
    def create_task3_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        label = QLabel("Задания 6-8: Работа с потоками и сигналами")
        label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(label)

        # Создаем новый поток при запуске
        self.worker_thread = None

        # Элементы управления
        btn_layout = QHBoxLayout()

        self.thread_start_btn = QPushButton("Запустить поток")
        self.thread_start_btn.clicked.connect(self.start_worker_thread)

        self.thread_stop_btn = QPushButton("Остановить поток")
        self.thread_stop_btn.clicked.connect(self.stop_worker_thread)
        self.thread_stop_btn.setEnabled(False)

        btn_layout.addWidget(self.thread_start_btn)
        btn_layout.addWidget(self.thread_stop_btn)
        layout.addLayout(btn_layout)

        # Отображение данных из потока
        self.thread_output = QTextEdit()
        self.thread_output.setReadOnly(True)
        layout.addWidget(QLabel("Данные из потока:"))
        layout.addWidget(self.thread_output)

        # Прогресс из потока
        self.thread_progress = QProgressBar()
        layout.addWidget(self.thread_progress)

        # Статус потока
        self.thread_status = QLabel("Поток не запущен")
        layout.addWidget(self.thread_status)

        self.tab_widget.addTab(tab, "Задания 6-8")

    def start_worker_thread(self):
        # Создаем новый экземпляр потока каждый раз
        self.worker_thread = WorkerThread()

        # Подключаем сигналы
        self.worker_thread.progress_signal.connect(self.update_thread_progress)
        self.worker_thread.data_signal.connect(self.update_thread_output)
        self.worker_thread.status_signal.connect(self.update_thread_status)
        self.worker_thread.finished.connect(self.on_worker_thread_finished)

        # Запускаем поток
        self.worker_thread.start()

        # Обновляем UI
        self.thread_start_btn.setEnabled(False)
        self.thread_stop_btn.setEnabled(True)
        self.thread_status.setText("Поток запущен")
        self.thread_output.clear()
        self.thread_progress.setValue(0)

    def stop_worker_thread(self):
        if self.worker_thread and self.worker_thread.isRunning():
            self.worker_thread.stop()
            self.thread_status.setText("Остановка потока...")

    def update_thread_progress(self, value):
        self.thread_progress.setValue(value)

    def update_thread_output(self, data):
        self.thread_output.append(f"Поток: {data}")
        # Прокрутка вниз
        scrollbar = self.thread_output.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def update_thread_status(self, status):
        self.thread_status.setText(f"Статус: {status}")

    def on_worker_thread_finished(self):
        self.thread_start_btn.setEnabled(True)
        self.thread_stop_btn.setEnabled(False)
        self.thread_status.setText("Поток завершен")


# Класс потока для вывода в консоль
class OutputThread(QThread):
    output_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._running = True
        self._paused = False

    def run(self):
        while self._running:
            if not self._paused:
                self.output_signal.emit("*")
                print("*", end='', flush=True)
            self.msleep(100)  # Задержка 100 мс

    def stop(self):
        self._running = False
        self.wait()  # Ждем завершения потока

    def pause(self):
        self._paused = True

    def resume(self):
        self._paused = False


# Класс для длительных операций
class LongOperationThread(QThread):
    progress_signal = pyqtSignal(int)

    def __init__(self, op_type="long"):
        super().__init__()
        self.op_type = op_type

    def run(self):
        if self.op_type == "long":
            # Длительная операция
            for i in range(101):
                self.msleep(50)  # Имитация работы
                self.progress_signal.emit(i)
        else:
            # Разбитая операция
            for chunk in range(10):
                for i in range(10):
                    self.msleep(10)  # Короткая задача
                self.progress_signal.emit((chunk + 1) * 10)


# 6-8. Класс рабочего потока с сигналами
class WorkerThread(QThread):
    progress_signal = pyqtSignal(int)
    data_signal = pyqtSignal(str)
    status_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._running = True

    def run(self):
        self.status_signal.emit("Поток начал работу")

        for i in range(101):
            if not self._running:
                break

            # Имитация работы
            self.msleep(50)

            # Отправка прогресса
            self.progress_signal.emit(i)

            # Отправка данных
            if i % 10 == 0:
                self.data_signal.emit(f"Шаг {i} выполнен")

        if self._running:
            self.status_signal.emit("Поток завершил работу")
        else:
            self.status_signal.emit("Поток остановлен")

    def stop(self):
        self._running = False
        self.wait()  # Ждем завершения потока


# 2. Повторное использование кода через наследование
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


# Основная функция
def main():
    app = QApplication(sys.argv)

    # Настройка стиля приложения
    app.setStyle("Fusion")

    # Создание и отображение главного окна
    window = MainWindow()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()