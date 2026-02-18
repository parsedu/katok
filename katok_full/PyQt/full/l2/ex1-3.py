import sys
import random
import time
from datetime import datetime

from PyQt5 import QtCore, QtWidgets

import threading

from PyQt5.QtCore import QMetaObject, Qt, Q_ARG, QThread, pyqtSignal, QMutex, QMutexLocker, QTimer
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QTabWidget, QWidget, QLabel, QHBoxLayout, QPushButton, QTextEdit, \
    QApplication, QProgressBar, QGridLayout
from queue import Queue, LifoQueue, PriorityQueue


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Лабораторная работа №2")
        self.setGeometry(100, 100, 900, 700)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)

        self.create_queue_tab()
        self.create_stack_tab()
        self.create_priority_queue_tab()

        self.show()

    def create_queue_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        title = QLabel("1. Очередь Queue (FIFO)")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        self.queue = Queue()
        self.queue_history = QTextEdit()
        self.queue_history.setReadOnly(True)
        layout.addWidget(QLabel("Содержимое очереди:"))
        layout.addWidget(self.queue_history)

        controls = QHBoxLayout()

        enqueue_btn = QPushButton("Добавить (enqueue)")
        enqueue_btn.clicked.connect(self.enqueue_item)

        dequeue_btn = QPushButton("Извлечь (dequeue)")
        dequeue_btn.clicked.connect(self.dequeue_item)

        clear_btn = QPushButton("Очистить очередь")
        clear_btn.clicked.connect(self.clear_queue)

        controls.addWidget(enqueue_btn)
        controls.addWidget(dequeue_btn)
        controls.addWidget(clear_btn)

        layout.addLayout(controls)

        self.queue_size_label = QLabel("Размер очереди: 0")
        layout.addWidget(self.queue_size_label)

        self.queue_preview = QLabel("Первый элемент: очередь пуста")
        layout.addWidget(self.queue_preview)

        self.tab_widget.addTab(tab, "Queue")

    def enqueue_item(self):
        item = f"Элемент-{random.randint(100, 999)}"
        self.queue.put(item)
        self.update_queue_display()

    def dequeue_item(self):
        if not self.queue.empty():
            item = self.queue.get()
            self.queue_history.append(f"Извлечено: {item}")
            self.update_queue_display()
        else:
            self.queue_history.append("Очередь пуста!")

    def clear_queue(self):
        while not self.queue.empty():
            self.queue.get()
        self.queue_history.clear()
        self.update_queue_display()

    def update_queue_display(self):
        items = list(self.queue.queue)
        self.queue_history.clear()
        if items:
            for i, item in enumerate(items):
                self.queue_history.append(f"{i + 1}. {item}")
        else:
            self.queue_history.append("Очередь пуста")

        self.queue_size_label.setText(f"Размер очереди: {self.queue.qsize()}")

        if not self.queue.empty():
            self.queue_preview.setText(f"Первый элемент: {next(iter(self.queue.queue))}")
        else:
            self.queue_preview.setText("Первый элемент: очередь пуста")

    def create_stack_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        title = QLabel("2. Стек LifoQueue (LIFO)")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        self.stack = LifoQueue()
        self.stack_history = QTextEdit()
        self.stack_history.setReadOnly(True)
        layout.addWidget(QLabel("Содержимое стека:"))
        layout.addWidget(self.stack_history)

        controls = QHBoxLayout()

        push_btn = QPushButton("Push (добавить)")
        push_btn.clicked.connect(self.push_item)

        pop_btn = QPushButton("Pop (извлечь)")
        pop_btn.clicked.connect(self.pop_item)

        peek_btn = QPushButton("Peek (посмотреть верхний)")
        peek_btn.clicked.connect(self.peek_stack)

        controls.addWidget(push_btn)
        controls.addWidget(pop_btn)
        controls.addWidget(peek_btn)

        layout.addLayout(controls)

        self.stack_size_label = QLabel("Размер стека: 0")
        layout.addWidget(self.stack_size_label)

        self.tab_widget.addTab(tab, "Stack")

    def push_item(self):
        item = f"Элемент-{random.randint(100, 999)}"
        self.stack.put(item)
        self.update_stack_display()

    def pop_item(self):
        if not self.stack.empty():
            item = self.stack.get()
            self.stack_history.append(f"Извлечено: {item}")
            self.update_stack_display()
        else:
            self.stack_history.append("Стек пуст!")

    def peek_stack(self):
        if not self.stack.empty():
            items = list(self.stack.queue)
            top_item = items[-1]
            self.stack_history.append(f"Верхний элемент: {top_item}")
        else:
            self.stack_history.append("Стек пуст!")

    def update_stack_display(self):
        items = list(self.stack.queue)
        self.stack_history.clear()
        if items:
            for i, item in enumerate(reversed(items)):
                self.stack_history.append(f"{i + 1}. {item}")
        else:
            self.stack_history.append("Стек пуст")

        self.stack_size_label.setText(f"Размер стека: {self.stack.qsize()}")

    def create_priority_queue_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        title = QLabel("3. Очередь с приоритетом PriorityQueue")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        self.priority_queue = PriorityQueue()
        self.pq_history = QTextEdit()
        self.pq_history.setReadOnly(True)
        layout.addWidget(QLabel("Содержимое очереди (приоритет : значение):"))
        layout.addWidget(self.pq_history)

        controls = QGridLayout()

        add_low_btn = QPushButton("Добавить низкий приоритет")
        add_low_btn.clicked.connect(lambda: self.add_to_priority_queue(3))

        add_medium_btn = QPushButton("Добавить средний приоритет")
        add_medium_btn.clicked.connect(lambda: self.add_to_priority_queue(2))

        add_high_btn = QPushButton("Добавить высокий приоритет")
        add_high_btn.clicked.connect(lambda: self.add_to_priority_queue(1))

        get_btn = QPushButton("Извлечь элемент")
        get_btn.clicked.connect(self.get_from_priority_queue)

        controls.addWidget(add_high_btn, 0, 0)
        controls.addWidget(add_medium_btn, 0, 1)
        controls.addWidget(add_low_btn, 0, 2)
        controls.addWidget(get_btn, 1, 0, 1, 3)

        layout.addLayout(controls)

        self.pq_size_label = QLabel("Размер очереди: 0")
        layout.addWidget(self.pq_size_label)

        explanation = QLabel("Приоритеты: 1 - высокий, 2 - средний, 3 - низкий")
        explanation.setStyleSheet("color: gray; font-style: italic;")
        layout.addWidget(explanation)

        self.tab_widget.addTab(tab, "PriorityQueue")

    def add_to_priority_queue(self, priority):
        item = f"Задача-{random.randint(100, 999)}"
        self.priority_queue.put((priority, item))
        self.update_priority_queue_display()

    def get_from_priority_queue(self):
        if not self.priority_queue.empty():
            priority, item = self.priority_queue.get()
            priority_text = {1: "Высокий", 2: "Средний", 3: "Низкий"}[priority]
            self.pq_history.append(f"Извлечено: [{priority_text}] {item}")
            self.update_priority_queue_display()
        else:
            self.pq_history.append("Очередь пуста!")

    def update_priority_queue_display(self):
        items = list(self.priority_queue.queue)
        self.pq_history.clear()
        if items:
            sorted_items = sorted(items, key=lambda x: x[0])
            for priority, item in sorted_items:
                priority_text = {1: "Высокий", 2: "Средний", 3: "Низкий"}[priority]
                self.pq_history.append(f"{priority_text}: {item}")
        else:
            self.pq_history.append("Очередь пуста")

        self.pq_size_label.setText(f"Размер очереди: {self.priority_queue.qsize()}")

    def create_queue_methods_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        title = QLabel("4. Методы модуля queue")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        self.demo_queue = Queue(maxsize=5)
        self.methods_history = QTextEdit()
        self.methods_history.setReadOnly(True)
        layout.addWidget(QLabel("Результаты выполнения методов:"))
        layout.addWidget(self.methods_history)

        grid = QGridLayout()

        methods = [
            ("qsize()", self.demo_qsize),
            ("empty()", self.demo_empty),
            ("full()", self.demo_full),
            ("put_nowait()", self.demo_put_nowait),
            ("get_nowait()", self.demo_get_nowait),
            ("put() с таймаутом", self.demo_put_timeout),
            ("get() с таймаутом", self.demo_get_timeout),
            ("Заполнить очередь", self.fill_queue),
            ("Очистить очередь", self.clear_demo_queue)
        ]

        for i, (name, func) in enumerate(methods):
            btn = QPushButton(name)
            btn.clicked.connect(func)
            grid.addWidget(btn, i // 3, i % 3)

        layout.addLayout(grid)

        self.demo_status = QLabel("Статус: очередь пуста")
        layout.addWidget(self.demo_status)

        self.tab_widget.addTab(tab, "Методы Queue")

    def demo_qsize(self):
        size = self.demo_queue.qsize()
        self.methods_history.append(f"qsize() = {size}")
        self.update_demo_status()

    def demo_empty(self):
        empty = self.demo_queue.empty()
        self.methods_history.append(f"empty() = {empty}")

    def demo_full(self):
        full = self.demo_queue.full()
        self.methods_history.append(f"full() = {full}")

    def demo_put_nowait(self):
        try:
            item = f"Эл-{random.randint(10, 99)}"
            self.demo_queue.put_nowait(item)
            self.methods_history.append(f"put_nowait('{item}') - успешно")
        except Exception as e:
            self.methods_history.append(f"put_nowait() - ошибка: {e}")
        self.update_demo_status()

    def demo_get_nowait(self):
        try:
            item = self.demo_queue.get_nowait()
            self.methods_history.append(f"get_nowait() = '{item}'")
        except Exception as e:
            self.methods_history.append(f"get_nowait() - ошибка: {e}")
        self.update_demo_status()

    def demo_put_timeout(self):
        try:
            item = f"Тайм-{random.randint(10, 99)}"
            self.demo_queue.put(item, timeout=1)
            self.methods_history.append(f"put('{item}', timeout=1) - успешно")
        except Exception as e:
            self.methods_history.append(f"put(timeout=1) - ошибка: {e}")
        self.update_demo_status()

    def demo_get_timeout(self):
        try:
            item = self.demo_queue.get(timeout=1)
            self.methods_history.append(f"get(timeout=1) = '{item}'")
        except Exception as e:
            self.methods_history.append(f"get(timeout=1) - ошибка: {e}")
        self.update_demo_status()

    def fill_queue(self):
        while not self.demo_queue.full():
            item = f"Зап-{random.randint(100, 999)}"
            self.demo_queue.put(item)
        self.methods_history.append("Очередь заполнена")
        self.update_demo_status()

    def clear_demo_queue(self):
        while not self.demo_queue.empty():
            self.demo_queue.get()
        self.methods_history.append("Очередь очищена")
        self.update_demo_status()

    def update_demo_status(self):
        size = self.demo_queue.qsize()
        maxsize = self.demo_queue.maxsize
        self.demo_status.setText(f"Статус: {size}/{maxsize} элементов")

    def create_mutex_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        title = QLabel("5-7. Синхронизация: QMutex, QMutexLocker, with..as")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        self.shared_counter = 0
        self.mutex = QMutex()
        self.counter_label = QLabel("Счетчик: 0")
        self.counter_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(self.counter_label)

        self.mutex_history = QTextEdit()
        self.mutex_history.setReadOnly(True)
        layout.addWidget(QLabel("Лог операций:"))
        layout.addWidget(self.mutex_history)

        grid = QGridLayout()

        inc_mutex_btn = QPushButton("Инкремент с QMutex")
        inc_mutex_btn.clicked.connect(self.increment_with_mutex)

        dec_mutex_btn = QPushButton("Декремент с QMutex")
        dec_mutex_btn.clicked.connect(self.decrement_with_mutex)

        inc_locker_btn = QPushButton("Инкремент с QMutexLocker")
        inc_locker_btn.clicked.connect(self.increment_with_locker)

        dec_locker_btn = QPushButton("Декремент с QMutexLocker")
        dec_locker_btn.clicked.connect(self.decrement_with_locker)

        inc_with_btn = QPushButton("Инкремент с with..as")
        inc_with_btn.clicked.connect(self.increment_with_context)

        dec_with_btn = QPushButton("Декремент с with..as")
        dec_with_btn.clicked.connect(self.decrement_with_context)

        race_btn = QPushButton("Тест гонки данных (без синхронизации)")
        race_btn.clicked.connect(self.test_race_condition)

        sync_btn = QPushButton("Тест с синхронизацией")
        sync_btn.clicked.connect(self.test_with_synchronization)

        grid.addWidget(inc_mutex_btn, 0, 0)
        grid.addWidget(dec_mutex_btn, 0, 1)
        grid.addWidget(inc_locker_btn, 1, 0)
        grid.addWidget(dec_locker_btn, 1, 1)
        grid.addWidget(inc_with_btn, 2, 0)
        grid.addWidget(dec_with_btn, 2, 1)
        grid.addWidget(race_btn, 3, 0)
        grid.addWidget(sync_btn, 3, 1)

        layout.addLayout(grid)

        threads_layout = QHBoxLayout()

        self.thread1_status = QLabel("Поток 1: не активен")
        self.thread2_status = QLabel("Поток 2: не активен")

        threads_layout.addWidget(self.thread1_status)
        threads_layout.addWidget(self.thread2_status)

        layout.addLayout(threads_layout)

        self.tab_widget.addTab(tab, "Синхронизация")

    def increment_with_mutex(self):
        self.mutex.lock()
        try:
            old_value = self.shared_counter
            time.sleep(0.01)
            self.shared_counter += 1
            self.mutex_history.append(f"Инкремент: {old_value} -> {self.shared_counter}")
            self.update_counter_display()
        finally:
            self.mutex.unlock()

    def decrement_with_mutex(self):
        self.mutex.lock()
        try:
            old_value = self.shared_counter
            time.sleep(0.01)
            self.shared_counter -= 1
            self.mutex_history.append(f"Декремент: {old_value} -> {self.shared_counter}")
            self.update_counter_display()
        finally:
            self.mutex.unlock()

    def increment_with_locker(self):
        with QMutexLocker(self.mutex):
            old_value = self.shared_counter
            time.sleep(0.01)
            self.shared_counter += 1
            self.mutex_history.append(f"Инкремент (locker): {old_value} -> {self.shared_counter}")
            self.update_counter_display()

    def decrement_with_locker(self):
        with QMutexLocker(self.mutex):
            old_value = self.shared_counter
            time.sleep(0.01)
            self.shared_counter -= 1
            self.mutex_history.append(f"Декремент (locker): {old_value} -> {self.shared_counter}")
            self.update_counter_display()

    def increment_with_context(self):
        self.mutex.lock()
        try:
            old_value = self.shared_counter
            time.sleep(0.01)
            self.shared_counter += 1
            self.mutex_history.append(f"Инкремент (with): {old_value} -> {self.shared_counter}")
            self.update_counter_display()
        finally:
            self.mutex.unlock()

    def decrement_with_context(self):
        self.mutex.lock()
        try:
            old_value = self.shared_counter
            time.sleep(0.01)
            self.shared_counter -= 1
            self.mutex_history.append(f"Декремент (with): {old_value} -> {self.shared_counter}")
            self.update_counter_display()
        finally:
            self.mutex.unlock()

    def test_race_condition(self):
        self.shared_counter = 0
        self.mutex_history.append("\n=== Тест гонки данных (без синхронизации) ===")

        def worker_increment():
            for _ in range(50):
                old = self.shared_counter
                time.sleep(0.001)
                self.shared_counter = old + 1

        def worker_decrement():
            for _ in range(50):
                old = self.shared_counter
                time.sleep(0.001)
                self.shared_counter = old - 1

        from threading import Thread
        t1 = Thread(target=worker_increment)
        t2 = Thread(target=worker_decrement)

        t1.start()
        t2.start()
        t1.join()
        t2.join()

        self.mutex_history.append(f"Результат: {self.shared_counter} (должно быть 0)")
        self.update_counter_display()

    def test_with_synchronization(self):
        self.shared_counter = 0
        self.mutex_history.append("\n=== Тест с синхронизацией ===")

        def worker_increment_sync():
            for _ in range(50):
                self.mutex.lock()
                try:
                    old = self.shared_counter
                    time.sleep(0.001)
                    self.shared_counter = old + 1
                finally:
                    self.mutex.unlock()

        def worker_decrement_sync():
            for _ in range(50):
                self.mutex.lock()
                try:
                    old = self.shared_counter
                    time.sleep(0.001)
                    self.shared_counter = old - 1
                finally:
                    self.mutex.unlock()

        from threading import Thread
        t1 = Thread(target=worker_increment_sync)
        t2 = Thread(target=worker_decrement_sync)

        t1.start()
        t2.start()
        t1.join()
        t2.join()

        self.mutex_history.append(f"Результат: {self.shared_counter} (корректно: 0)")
        self.update_counter_display()

    def update_counter_display(self):
        self.counter_label.setText(f"Счетчик: {self.shared_counter}")
        QApplication.processEvents()

    def create_splash_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        title = QLabel("8. Вывод заставки")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        self.splash_display = QLabel()
        self.splash_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splash_display.setStyleSheet("""
            border: 2px solid #ccc;
            border-radius: 10px;
            background-color: #f0f0f0;
            min-height: 200px;
        """)
        layout.addWidget(self.splash_display)

        controls = QHBoxLayout()

        show_text_btn = QPushButton("Показать текстовую заставку")
        show_text_btn.clicked.connect(self.show_text_splash)

        show_animated_btn = QPushButton("Показать анимированную заставку")
        show_animated_btn.clicked.connect(self.show_animated_splash)

        show_custom_btn = QPushButton("Показать кастомную заставку")
        show_custom_btn.clicked.connect(self.show_custom_splash)

        clear_btn = QPushButton("Очистить")
        clear_btn.clicked.connect(self.clear_splash)

        controls.addWidget(show_text_btn)
        controls.addWidget(show_animated_btn)
        controls.addWidget(show_custom_btn)
        controls.addWidget(clear_btn)

        layout.addLayout(controls)

        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self.update_animation)
        self.animation_frame = 0

        self.tab_widget.addTab(tab, "Заставка")

    def show_text_splash(self):
        splash_text = """
        <div style='text-align: center;'>
            <h1 style='color: #4CAF50;'>Лабораторная работа №2</h1>
            <h2 style='color: #2196F3;'>Структуры данных и синхронизация</h2>
            <p style='font-size: 16px;'>Разработано на PyQt5</p>
            <p style='font-size: 14px; color: #666;'>
                Очереди, стеки, мьютексы<br>
                и другие структуры данных
            </p>
        </div>
        """
        self.splash_display.setText(splash_text)

    def show_animated_splash(self):
        self.animation_frame = 0
        self.animation_timer.start(100)

    def update_animation(self):
        self.animation_frame += 1
        if self.animation_frame > 20:
            self.animation_timer.stop()
            return

        progress = self.animation_frame / 20
        width = int(progress * 300)

        animation_html = f"""
        <div style='text-align: center;'>
            <h3 style='color: #FF5722;'>Загрузка...</h3>
            <div style='
                width: 300px;
                height: 20px;
                border: 1px solid #ccc;
                margin: 20px auto;
                background: linear-gradient(90deg, #4CAF50 {width}px, #f0f0f0 {width}px);
                border-radius: 10px;
            '></div>
            <p>Выполнение: {self.animation_frame * 5}%</p>
            {'✓' * self.animation_frame}{'○' * (20 - self.animation_frame)}
        </div>
        """
        self.splash_display.setText(animation_html)

    def show_custom_splash(self):
        now = datetime.now()
        custom_html = f"""
        <div style='text-align: center; padding: 20px;'>
            <div style='
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 15px;
                padding: 30px;
                color: white;
                box-shadow: 0 10px 20px rgba(0,0,0,0.2);
            '>
                <h1 style='margin: 0;'>PyQt5 Demo</h1>
                <h3 style='margin: 10px 0 20px 0;'>Лабораторная работа</h3>

                <div style='
                    display: flex;
                    justify-content: space-around;
                    margin: 20px 0;
                '>
                    <div style='text-align: center;'>
                        <div style='
                            background: rgba(255,255,255,0.2);
                            border-radius: 50%;
                            width: 60px;
                            height: 60px;
                            line-height: 60px;
                            margin: 0 auto 10px;
                            font-size: 24px;
                        '>Q</div>
                        <div>Queue</div>
                    </div>

                    <div style='text-align: center;'>
                        <div style='
                            background: rgba(255,255,255,0.2);
                            border-radius: 50%;
                            width: 60px;
                            height: 60px;
                            line-height: 60px;
                            margin: 0 auto 10px;
                            font-size: 24px;
                        '>S</div>
                        <div>Stack</div>
                    </div>

                    <div style='text-align: center;'>
                        <div style='
                            background: rgba(255,255,255,0.2);
                            border-radius: 50%;
                            width: 60px;
                            height: 60px;
                            line-height: 60px;
                            margin: 0 auto 10px;
                            font-size: 24px;
                        '>M</div>
                        <div>Mutex</div>
                    </div>
                </div>

                <div style='
                    border-top: 1px solid rgba(255,255,255,0.3);
                    padding-top: 15px;
                    font-size: 12px;
                    opacity: 0.8;
                '>
                    Время: {now.strftime("%H:%M:%S")}<br>
                    Дата: {now.strftime("%d.%m.%Y")}
                </div>
            </div>
        </div>
        """
        self.splash_display.setText(custom_html)

    def clear_splash(self):
        self.splash_display.clear()
        self.animation_timer.stop()


def main():
    app = QApplication(sys.argv)

    app.setStyle("Fusion")

    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(240, 240, 240))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(0, 0, 0))
    app.setPalette(palette)

    window = MainWindow()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()