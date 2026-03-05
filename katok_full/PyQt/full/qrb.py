import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QGroupBox, QRadioButton, QLabel, QButtonGroup)
from PyQt5.QtCore import Qt


class ConsoleOutputTask(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Задание")
        self.setGeometry(200, 200, 300, 250)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        label = QLabel("Выберите пункт для вывода данных в консоль:")
        main_layout.addWidget(label)

        group_box = QGroupBox("Пункты меню")
        layout = QVBoxLayout()

        self.option1 = QRadioButton("Пункт 1")
        self.option2 = QRadioButton("Пункт 2")
        self.option3 = QRadioButton("Пункт 3")
        self.option4 = QRadioButton("Пункт 4")

        group = QButtonGroup(self)
        group.addButton(self.option1)
        group.addButton(self.option2)
        group.addButton(self.option3)
        group.addButton(self.option4)

        self.option1.toggled.connect(self.on_option_selected)
        self.option2.toggled.connect(self.on_option_selected)
        self.option3.toggled.connect(self.on_option_selected)
        self.option4.toggled.connect(self.on_option_selected)

        layout.addWidget(self.option1)
        layout.addWidget(self.option2)
        layout.addWidget(self.option3)
        layout.addWidget(self.option4)
        group_box.setLayout(layout)
        main_layout.addWidget(group_box)

    def on_option_selected(self, checked):
        if checked:
            self.print_data(self.sender().text())

    def print_data(self, option):
        print(f"\n--- {option} ---")

        if option == "Пункт 1":
            print("Данные 1: 10, 20, 30")
        elif option == "Пункт 2":
            print("Данные 2: A, B, C")
        elif option == "Пункт 3":
            print("Данные 3: true, false")
        elif option == "Пункт 4":
            print("Данные 4: тестовые данные")


app = QApplication(sys.argv)
window = ConsoleOutputTask()
window.show()
sys.exit(app.exec())