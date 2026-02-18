import sys
import time
from PyQt5 import QtCore, QtWidgets
import threading

from PyQt5.QtCore import QMetaObject, Qt, Q_ARG, QThread, pyqtSignal, QEvent, QRectF, QPoint, QTimer
from PyQt5.QtGui import QColor, QIcon, QPainterPath, QRegion, QPolygon
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QTabWidget, QWidget, QLabel, QHBoxLayout, QPushButton, QTextEdit, \
    QApplication, QProgressBar, QGridLayout, QSlider, QDialog, QStyle, QMessageBox
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Лабораторная работа №3")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)

        self.create_window_tab()
        self.create_position_tab()
        self.create_minmax_tab()
        self.create_transparency_tab()
        self.create_modal_tab()
        self.create_icon_tab()
        self.create_color_tab()
        self.create_image_tab()
        self.create_shape_tab()
        self.create_tooltip_tab()
        self.create_close_tab()

        self.show()

    def create_window_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        title = QLabel("1. Создание и отображение окна")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        info = QLabel("Это окно создано с помощью PyQt.\nОсновное окно наследуется от QMainWindow.")
        layout.addWidget(info)

        self.tab_widget.addTab(tab, "1. Создание окна")


    def create_position_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        title = QLabel("2. Получение размеров и местоположение окна")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        self.pos_info = QLabel()
        layout.addWidget(self.pos_info)

        self.update_pos_info()

        grid = QGridLayout()

        move_btn = QPushButton("Переместить в (100, 100)")
        move_btn.clicked.connect(lambda: self.move(100, 100))

        move_center_btn = QPushButton("Переместить в центр")
        move_center_btn.clicked.connect(self.move_to_center)

        move_random_btn = QPushButton("Случайное положение")
        move_random_btn.clicked.connect(self.move_random)

        get_pos_btn = QPushButton("Получить положение")
        get_pos_btn.clicked.connect(self.show_position)

        get_frame_btn = QPushButton("Получить frameGeometry")
        get_frame_btn.clicked.connect(self.show_frame_geometry)

        grid.addWidget(move_btn, 0, 0)
        grid.addWidget(move_center_btn, 0, 1)
        grid.addWidget(move_random_btn, 0, 2)
        grid.addWidget(get_pos_btn, 1, 0)
        grid.addWidget(get_frame_btn, 1, 1)

        layout.addLayout(grid)

        self.position_label = QLabel()
        self.frame_label = QLabel()

        layout.addWidget(self.position_label)
        layout.addWidget(self.frame_label)

        self.tab_widget.addTab(tab, "2. Положение")

    def update_pos_info(self):
        pos = self.pos()
        self.pos_info.setText(f"Положение окна: x={pos.x()}, y={pos.y()}")

    def move_to_center(self):
        screen = QApplication.primaryScreen().geometry()
        window = self.geometry()
        x = (screen.width() - window.width()) // 2
        y = (screen.height() - window.height()) // 2
        self.move(x, y)

    def move_random(self):
        screen = QApplication.primaryScreen().geometry()
        x = random.randint(0, screen.width() - self.width())
        y = random.randint(0, screen.height() - self.height())
        self.move(x, y)

    def show_position(self):
        pos = self.pos()
        self.position_label.setText(f"pos(): x={pos.x()}, y={pos.y()}")

    def show_frame_geometry(self):
        frame = self.frameGeometry()
        self.frame_label.setText(f"frameGeometry(): x={frame.x()}, y={frame.y()}, "
                                 f"width={frame.width()}, height={frame.height()}")

    def moveEvent(self, event):
        self.update_pos_info()
        super().moveEvent(event)

    def create_minmax_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        title = QLabel("3. Сворачивание и разворачивание окон")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        grid = QGridLayout()

        minimize_btn = QPushButton("Свернуть")
        minimize_btn.clicked.connect(self.showMinimized)

        maximize_btn = QPushButton("Развернуть")
        maximize_btn.clicked.connect(self.showMaximized)

        normal_btn = QPushButton("Обычный размер")
        normal_btn.clicked.connect(self.showNormal)

        fullscreen_btn = QPushButton("Полный экран")
        fullscreen_btn.clicked.connect(self.toggle_fullscreen)

        grid.addWidget(minimize_btn, 0, 0)
        grid.addWidget(maximize_btn, 0, 1)
        grid.addWidget(normal_btn, 1, 0)
        grid.addWidget(fullscreen_btn, 1, 1)

        layout.addLayout(grid)

        self.window_state_label = QLabel("Состояние окна: нормальное")
        layout.addWidget(self.window_state_label)

        self.tab_widget.addTab(tab, "3. Свернуть/Развернуть")

    def toggle_fullscreen(self):
        if self.windowState() & Qt.WindowState.WindowFullScreen:
            self.showNormal()
        else:
            self.showFullScreen()

    def changeEvent(self, event):
        if event.type() == QEvent.Type.WindowStateChange:
            state = self.windowState()
            if state & Qt.WindowState.WindowMinimized:
                self.window_state_label.setText("Состояние окна: свернуто")
            elif state & Qt.WindowState.WindowMaximized:
                self.window_state_label.setText("Состояние окна: развернуто")
            elif state & Qt.WindowState.WindowFullScreen:
                self.window_state_label.setText("Состояние окна: полный экран")
            else:
                self.window_state_label.setText("Состояние окна: нормальное")

        super().changeEvent(event)

    def create_transparency_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        title = QLabel("4. Управление прозрачностью окна")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        self.opacity_slider = QSlider(Qt.Orientation.Horizontal)
        self.opacity_slider.setRange(10, 100)
        self.opacity_slider.setValue(100)
        self.opacity_slider.valueChanged.connect(self.change_opacity)

        layout.addWidget(QLabel("Непрозрачность:"))
        layout.addWidget(self.opacity_slider)

        self.opacity_label = QLabel("100%")
        layout.addWidget(self.opacity_label)

        buttons_layout = QHBoxLayout()

        opaque_btn = QPushButton("100%")
        opaque_btn.clicked.connect(lambda: self.set_opacity(100))

        half_btn = QPushButton("50%")
        half_btn.clicked.connect(lambda: self.set_opacity(50))

        quarter_btn = QPushButton("25%")
        quarter_btn.clicked.connect(lambda: self.set_opacity(25))

        buttons_layout.addWidget(opaque_btn)
        buttons_layout.addWidget(half_btn)
        buttons_layout.addWidget(quarter_btn)

        layout.addLayout(buttons_layout)

        self.tab_widget.addTab(tab, "4. Прозрачность")

    def change_opacity(self, value):
        opacity = value / 100.0
        self.setWindowOpacity(opacity)
        self.opacity_label.setText(f"{value}%")

    def set_opacity(self, value):
        self.opacity_slider.setValue(value)

    def create_modal_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        title = QLabel("5. Модальное окно")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        modal_btn = QPushButton("Показать модальное окно")
        modal_btn.clicked.connect(self.show_modal_dialog)

        layout.addWidget(modal_btn)

        nonmodal_btn = QPushButton("Показать немодальное окно")
        nonmodal_btn.clicked.connect(self.show_nonmodal_dialog)

        layout.addWidget(nonmodal_btn)

        info = QLabel("Модальное окно блокирует доступ к родительскому окну.\n"
                      "Немодальное окно позволяет работать с обоими окнами одновременно.")
        info.setStyleSheet("background-color: #f0f0f0; padding: 10px; border-radius: 5px;")
        layout.addWidget(info)

        self.tab_widget.addTab(tab, "5. Модальные окна")

    def show_modal_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Модальное окно")
        dialog.setModal(True)

        layout = QVBoxLayout(dialog)
        layout.addWidget(QLabel("Это модальное окно!"))
        layout.addWidget(QLabel("Вы не можете работать с главным окном,\nпока не закроете это окно."))

        ok_btn = QPushButton("OK")
        ok_btn.clicked.connect(dialog.accept)
        layout.addWidget(ok_btn)

        dialog.exec()

    def show_nonmodal_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Немодальное окно")
        dialog.setModal(False)

        layout = QVBoxLayout(dialog)
        layout.addWidget(QLabel("Это немодальное окно!"))
        layout.addWidget(QLabel("Вы можете работать с обоими окнами одновременно."))

        close_btn = QPushButton("Закрыть")
        close_btn.clicked.connect(dialog.close)
        layout.addWidget(close_btn)

        dialog.show()

    def create_icon_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        title = QLabel("6. Смена значка в заголовке окна")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        grid = QGridLayout()

        icon1_btn = QPushButton("Иконка 1 (Qt)")
        icon1_btn.clicked.connect(lambda: self.setWindowIcon(self.style().standardIcon(
            QStyle.StandardPixmap.SP_ComputerIcon)))

        icon2_btn = QPushButton("Иконка 2 (Qt)")
        icon2_btn.clicked.connect(lambda: self.setWindowIcon(self.style().standardIcon(
            QStyle.StandardPixmap.SP_FileIcon)))

        icon3_btn = QPushButton("Иконка 3 (Qt)")
        icon3_btn.clicked.connect(lambda: self.setWindowIcon(self.style().standardIcon(
            QStyle.StandardPixmap.SP_DirIcon)))

        remove_btn = QPushButton("Удалить иконку")
        remove_btn.clicked.connect(lambda: self.setWindowIcon(QIcon()))

        grid.addWidget(icon1_btn, 0, 0)
        grid.addWidget(icon2_btn, 0, 1)
        grid.addWidget(icon3_btn, 1, 0)
        grid.addWidget(remove_btn, 1, 1)

        layout.addLayout(grid)

        self.tab_widget.addTab(tab, "6. Иконка")

    def create_color_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        title = QLabel("7. Изменение цвета фона окна")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        grid = QGridLayout()

        red_btn = QPushButton("Красный")
        red_btn.clicked.connect(lambda: self.set_background_color(QColor(255, 200, 200)))

        green_btn = QPushButton("Зеленый")
        green_btn.clicked.connect(lambda: self.set_background_color(QColor(200, 255, 200)))

        blue_btn = QPushButton("Синий")
        blue_btn.clicked.connect(lambda: self.set_background_color(QColor(200, 200, 255)))

        yellow_btn = QPushButton("Желтый")
        yellow_btn.clicked.connect(lambda: self.set_background_color(QColor(255, 255, 200)))

        random_btn = QPushButton("Случайный цвет")
        random_btn.clicked.connect(self.set_random_color)

        reset_btn = QPushButton("Сбросить цвет")
        reset_btn.clicked.connect(self.reset_background_color)

        grid.addWidget(red_btn, 0, 0)
        grid.addWidget(green_btn, 0, 1)
        grid.addWidget(blue_btn, 0, 2)
        grid.addWidget(yellow_btn, 1, 0)
        grid.addWidget(random_btn, 1, 1)
        grid.addWidget(reset_btn, 1, 2)

        layout.addLayout(grid)

        self.tab_widget.addTab(tab, "7. Цвет фона")

    def set_background_color(self, color):
        self.centralWidget().setStyleSheet(f"background-color: {color.name()};")

    def set_random_color(self):
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.set_background_color(color)

    def reset_background_color(self):
        self.centralWidget().setStyleSheet("")

    def create_image_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        title = QLabel("8. Вывод изображения в качестве фона")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        grid = QGridLayout()

        pattern_btn = QPushButton("Узорный фон")
        pattern_btn.clicked.connect(self.set_pattern_background)

        gradient_btn = QPushButton("Градиентный фон")
        gradient_btn.clicked.connect(self.set_gradient_background)

        reset_bg_btn = QPushButton("Сбросить фон")
        reset_bg_btn.clicked.connect(self.reset_background)

        grid.addWidget(pattern_btn, 0, 0)
        grid.addWidget(gradient_btn, 0, 1)
        grid.addWidget(reset_bg_btn, 0, 2)

        layout.addLayout(grid)

        self.tab_widget.addTab(tab, "8. Фон-изображение")

    def set_pattern_background(self):
        style = """
        background-color: #f0f0f0;
        background-image: linear-gradient(45deg, #ccc 25%, transparent 25%),
                          linear-gradient(-45deg, #ccc 25%, transparent 25%),
                          linear-gradient(45deg, transparent 75%, #ccc 75%),
                          linear-gradient(-45deg, transparent 75%, #ccc 75%);
        background-size: 20px 20px;
        background-position: 0 0, 0 10px, 10px -10px, -10px 0px;
        """
        self.centralWidget().setStyleSheet(style)

    def set_gradient_background(self):
        style = """
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                   stop:0 #667eea, stop:1 #764ba2);
        color: white;
        """
        self.centralWidget().setStyleSheet(style)

    def reset_background(self):
        self.centralWidget().setStyleSheet("")

    def create_shape_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        title = QLabel("9. Создание окна произвольной формы")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        grid = QGridLayout()

        circle_btn = QPushButton("Круглое окно")
        circle_btn.clicked.connect(self.set_circular_window)

        rounded_btn = QPushButton("Окно со скруглениями")
        rounded_btn.clicked.connect(self.set_rounded_window)

        triangle_btn = QPushButton("Треугольное окно")
        triangle_btn.clicked.connect(self.set_triangle_window)

        reset_shape_btn = QPushButton("Обычное окно")
        reset_shape_btn.clicked.connect(self.reset_window_shape)

        grid.addWidget(circle_btn, 0, 0)
        grid.addWidget(rounded_btn, 0, 1)
        grid.addWidget(triangle_btn, 1, 0)
        grid.addWidget(reset_shape_btn, 1, 1)

        layout.addLayout(grid)

        warning = QLabel("Внимание: Окно произвольной формы может работать некорректно\n"
                         "на некоторых системах. Для возврата к обычной форме\n"
                         "используйте кнопку 'Обычное окно'.")
        warning.setStyleSheet("color: #ff0000; font-weight: bold;")
        layout.addWidget(warning)

        self.tab_widget.addTab(tab, "9. Форма окна")

    def set_circular_window(self):
        self.setMask(self.create_circular_mask())
        self.set_background_color(QColor(100, 150, 200))

    def create_circular_mask(self):
        diameter = min(self.width(), self.height())
        mask = QRegion(0, 0, diameter, diameter, QRegion.RegionType.Ellipse)
        return mask

    def set_rounded_window(self):
        path = QPainterPath()
        path.addRoundedRect(QRectF(self.rect()), 50, 50)
        mask = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)
        self.set_background_color(QColor(150, 200, 100))

    def set_triangle_window(self):
        polygon = QPolygon([
            QPoint(self.width() // 2, 0),
            QPoint(self.width(), self.height()),
            QPoint(0, self.height())
        ])
        mask = QRegion(polygon)
        self.setMask(mask)
        self.set_background_color(QColor(200, 100, 150))

    def reset_window_shape(self):
        self.clearMask()
        self.reset_background_color()

    def create_tooltip_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        title = QLabel("10. Всплывающие подсказки")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        button1 = QPushButton("Кнопка с подсказкой")
        button1.setToolTip("Это простая подсказка для кнопки")

        button2 = QPushButton("Кнопка с HTML подсказкой")
        button2.setToolTip("<b>HTML подсказка</b><br>"
                           "<i>Можно использовать HTML теги</i><br>"
                           "<font color='red'>Красный текст</font>")

        button3 = QPushButton("Кнопка с длинной подсказкой")
        button3.setToolTip("Очень длинная подсказка, которая должна "
                           "автоматически переноситься на несколько строк, "
                           "чтобы уместиться на экране.")

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        self.setToolTipDuration(5000)

        info = QLabel("Наведите курсор на кнопки, чтобы увидеть подсказки.\n"
                      "Подсказки исчезнут через 5 секунд.")
        layout.addWidget(info)

        self.tab_widget.addTab(tab, "10. Подсказки")

    def create_close_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        title = QLabel("11. Закрытие окна из программы")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        close_btn = QPushButton("Закрыть окно")
        close_btn.clicked.connect(self.close)

        layout.addWidget(close_btn)

        quit_btn = QPushButton("Завершить приложение")
        quit_btn.clicked.connect(QApplication.quit)

        layout.addWidget(quit_btn)

        delayed_close_btn = QPushButton("Закрыть через 3 секунды")
        delayed_close_btn.clicked.connect(self.delayed_close)

        layout.addWidget(delayed_close_btn)

        confirm_close_btn = QPushButton("Закрыть с подтверждением")
        confirm_close_btn.clicked.connect(self.confirm_close)

        layout.addWidget(confirm_close_btn)

        self.tab_widget.addTab(tab, "11. Закрытие")

    def delayed_close(self):
        QTimer.singleShot(3000, self.close)

    def confirm_close(self):
        reply = QMessageBox.question(self, "Подтверждение",
                                     "Вы уверены, что хотите закрыть окно?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.close()


def main():
    app = QApplication(sys.argv)

    app.setStyle("Fusion")

    window = MainWindow()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()