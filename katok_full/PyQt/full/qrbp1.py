import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QGroupBox, QRadioButton, QLabel,
                             QButtonGroup, QTextEdit)
from PyQt5.QtCore import Qt


class SimpleRadioButtonExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пример 1: Простые переключатели")
        self.setGeometry(200, 200, 500, 400)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Главный layout
        main_layout = QVBoxLayout(central_widget)

        # Заголовок
        title = QLabel("Простой пример QRadioButton")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50; padding: 10px;")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # Группа переключателей
        group_box = QGroupBox("Выберите операционную систему:")
        group_box.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                font-size: 14px;
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
        """)

        # Layout для группы
        group_layout = QVBoxLayout()

        # Создание переключателей
        self.windows_rb = QRadioButton("Windows")
        self.linux_rb = QRadioButton("Linux")
        self.macos_rb = QRadioButton("macOS")

        # Группа кнопок для логической группировки
        button_group = QButtonGroup(self)
        button_group.addButton(self.windows_rb)
        button_group.addButton(self.linux_rb)
        button_group.addButton(self.macos_rb)

        # Добавление переключателей в layout
        group_layout.addWidget(self.windows_rb)
        group_layout.addWidget(self.linux_rb)
        group_layout.addWidget(self.macos_rb)

        # Подключение сигналов
        self.windows_rb.toggled.connect(self.on_radio_button_toggled)
        self.linux_rb.toggled.connect(self.on_radio_button_toggled)
        self.macos_rb.toggled.connect(self.on_radio_button_toggled)

        group_box.setLayout(group_layout)
        main_layout.addWidget(group_box)

        # Область вывода
        output_label = QLabel("Результат выбора:")
        output_label.setStyleSheet("font-weight: bold; margin-top: 10px;")
        main_layout.addWidget(output_label)

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setMaximumHeight(150)
        main_layout.addWidget(self.output_text)

        # Информация
        info_label = QLabel("Выберите один из вариантов выше")
        info_label.setStyleSheet("color: gray; font-style: italic; margin-top: 10px;")
        info_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(info_label)

    def on_radio_button_toggled(self, checked):
        """Обработчик изменения состояния переключателя"""
        if checked:
            sender = self.sender()
            self.output_text.append(f"✓ Выбрано: {sender.text()}")


def main():
    app = QApplication(sys.argv)
    window = SimpleRadioButtonExample()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()