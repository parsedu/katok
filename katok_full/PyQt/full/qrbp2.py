import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QGroupBox, QRadioButton, QLabel,
                             QButtonGroup, QTextEdit, QPushButton)
from PyQt5.QtCore import Qt


class StyledRadioButtonExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пример 2: Стилизованные переключатели")
        self.setGeometry(200, 200, 600, 500)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Главный layout
        main_layout = QVBoxLayout(central_widget)

        # Заголовок
        title = QLabel("Стилизованные QRadioButton")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #e74c3c; padding: 10px;")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # Горизонтальный layout для групп
        groups_layout = QHBoxLayout()

        # === Группа 1: Цвета ===
        self.create_color_group(groups_layout)

        # === Группа 2: Размеры ===
        self.create_size_group(groups_layout)

        main_layout.addLayout(groups_layout)

        # Кнопка для применения выбора
        self.apply_btn = QPushButton("Применить выбор")
        self.apply_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px;
                font-size: 14px;
                border-radius: 5px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        self.apply_btn.clicked.connect(self.apply_selection)
        main_layout.addWidget(self.apply_btn)

        # Область результата
        result_label = QLabel("Результат:")
        result_label.setStyleSheet("font-weight: bold; margin-top: 10px;")
        main_layout.addWidget(result_label)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setMaximumHeight(150)
        main_layout.addWidget(self.result_text)

    def create_color_group(self, parent_layout):
        """Создание группы выбора цвета"""
        color_group = QGroupBox("Выберите цвет")
        color_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                color: #3498db;
                border: 2px solid #3498db;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
            QRadioButton {
                spacing: 5px;
                padding: 5px;
            }
            QRadioButton::indicator {
                width: 15px;
                height: 15px;
            }
            QRadioButton::indicator:checked {
                background-color: #3498db;
                border: 2px solid #2980b9;
                border-radius: 8px;
            }
        """)

        layout = QVBoxLayout()

        # Создание переключателей цветов
        self.red_rb = QRadioButton("Красный")
        self.green_rb = QRadioButton("Зеленый")
        self.blue_rb = QRadioButton("Синий")
        self.yellow_rb = QRadioButton("Желтый")

        # Группа кнопок
        color_group_btns = QButtonGroup(self)
        color_group_btns.addButton(self.red_rb)
        color_group_btns.addButton(self.green_rb)
        color_group_btns.addButton(self.blue_rb)
        color_group_btns.addButton(self.yellow_rb)

        # Добавление в layout
        layout.addWidget(self.red_rb)
        layout.addWidget(self.green_rb)
        layout.addWidget(self.blue_rb)
        layout.addWidget(self.yellow_rb)

        # Установка начального выбора
        self.blue_rb.setChecked(True)

        color_group.setLayout(layout)
        parent_layout.addWidget(color_group)

    def create_size_group(self, parent_layout):
        """Создание группы выбора размера"""
        size_group = QGroupBox("Выберите размер")
        size_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                color: #e67e22;
                border: 2px solid #e67e22;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
            QRadioButton {
                spacing: 5px;
                padding: 5px;
            }
            QRadioButton::indicator {
                width: 15px;
                height: 15px;
            }
            QRadioButton::indicator:checked {
                background-color: #e67e22;
                border: 2px solid #d35400;
                border-radius: 8px;
            }
        """)

        layout = QVBoxLayout()

        # Создание переключателей размеров
        self.small_rb = QRadioButton("Маленький")
        self.medium_rb = QRadioButton("Средний")
        self.large_rb = QRadioButton("Большой")

        # Группа кнопок
        size_group_btns = QButtonGroup(self)
        size_group_btns.addButton(self.small_rb)
        size_group_btns.addButton(self.medium_rb)
        size_group_btns.addButton(self.large_rb)

        # Добавление в layout
        layout.addWidget(self.small_rb)
        layout.addWidget(self.medium_rb)
        layout.addWidget(self.large_rb)

        # Установка начального выбора
        self.medium_rb.setChecked(True)

        size_group.setLayout(layout)
        parent_layout.addWidget(size_group)

    def apply_selection(self):
        """Применение выбранных опций"""
        # Определяем выбранный цвет
        color = "не выбран"
        if self.red_rb.isChecked():
            color = "Красный"
        elif self.green_rb.isChecked():
            color = "Зеленый"
        elif self.blue_rb.isChecked():
            color = "Синий"
        elif self.yellow_rb.isChecked():
            color = "Желтый"

        # Определяем выбранный размер
        size = "не выбран"
        if self.small_rb.isChecked():
            size = "Маленький"
        elif self.medium_rb.isChecked():
            size = "Средний"
        elif self.large_rb.isChecked():
            size = "Большой"

        # Вывод результата
        self.result_text.append(f"✓ Выбран цвет: {color}")
        self.result_text.append(f"✓ Выбран размер: {size}")
        self.result_text.append("-" * 30)


def main():
    app = QApplication(sys.argv)
    window = StyledRadioButtonExample()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()