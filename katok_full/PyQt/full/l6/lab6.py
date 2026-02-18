import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Лабораторная работа №6 - События клавиатуры")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)

        self.create_focus_tab()
        self.create_key_events_tab()

        self.log_widget = QTextEdit()
        self.log_widget.setReadOnly(True)
        self.log_widget.setMaximumHeight(200)
        main_layout.addWidget(QLabel("Лог событий клавиатуры:"))
        main_layout.addWidget(self.log_widget)

        self.show()

    def log_event(self, message):
        timestamp = QDateTime.currentDateTime().toString("hh:mm:ss")
        self.log_widget.append(f"[{timestamp}] {message}")

    def create_focus_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        title = QLabel("1. Установка фокуса ввода")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)



        self.focus_status = QLabel("Фокус ввода: ни на одном виджете")
        self.focus_status.setStyleSheet("font-size: 14px; font-weight: bold; color: #2196F3;")
        layout.addWidget(self.focus_status)

        grid = QGridLayout()

        self.line_edit1 = QLineEdit()
        self.line_edit1.setPlaceholderText("Поле ввода 1")
        self.line_edit1.textChanged.connect(lambda text: self.log_event(f"Поле 1: '{text}'"))
        self.line_edit1.installEventFilter(self)

        self.line_edit2 = QLineEdit()
        self.line_edit2.setPlaceholderText("Поле ввода 2")
        self.line_edit2.textChanged.connect(lambda text: self.log_event(f"Поле 2: '{text}'"))
        self.line_edit2.installEventFilter(self)

        self.line_edit3 = QLineEdit()
        self.line_edit3.setPlaceholderText("Поле ввода 3")
        self.line_edit3.textChanged.connect(lambda text: self.log_event(f"Поле 3: '{text}'"))
        self.line_edit3.installEventFilter(self)

        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Многострочное текстовое поле")
        self.text_edit.setMaximumHeight(100)
        self.text_edit.installEventFilter(self)

        set_focus_btn1 = QPushButton("Фокус на поле 1")
        set_focus_btn1.clicked.connect(lambda: self.set_focus_on(self.line_edit1))

        set_focus_btn2 = QPushButton("Фокус на поле 2")
        set_focus_btn2.clicked.connect(lambda: self.set_focus_on(self.line_edit2))

        set_focus_btn3 = QPushButton("Фокус на поле 3")
        set_focus_btn3.clicked.connect(lambda: self.set_focus_on(self.line_edit3))

        set_focus_text = QPushButton("Фокус на текстовое поле")
        set_focus_text.clicked.connect(lambda: self.set_focus_on(self.text_edit))

        clear_focus_btn = QPushButton("Сбросить фокус")
        clear_focus_btn.clicked.connect(self.clear_focus)




        grid.addWidget(QLabel("Поле ввода 1:"), 0, 0)
        grid.addWidget(self.line_edit1, 0, 1)
        grid.addWidget(set_focus_btn1, 0, 2)

        grid.addWidget(QLabel("Поле ввода 2:"), 1, 0)
        grid.addWidget(self.line_edit2, 1, 1)
        grid.addWidget(set_focus_btn2, 1, 2)

        grid.addWidget(QLabel("Поле ввода 3:"), 2, 0)
        grid.addWidget(self.line_edit3, 2, 1)
        grid.addWidget(set_focus_btn3, 2, 2)

        grid.addWidget(QLabel("Текстовое поле:"), 3, 0)
        grid.addWidget(self.text_edit, 3, 1, 1, 2)

        grid.addWidget(set_focus_text, 4, 0)
        grid.addWidget(clear_focus_btn, 4, 1)


        layout.addLayout(grid)

        self.tab_order_label = QLabel("")
        layout.addWidget(self.tab_order_label)

        self.tab_widget.addTab(tab, "1. Фокус ввода")

    def set_focus_on(self, widget):
        widget.setFocus()
        self.update_focus_status()

    def clear_focus(self):
        focused_widget = QApplication.focusWidget()
        if focused_widget:
            focused_widget.clearFocus()
        self.update_focus_status()

    def update_focus_status(self):
        focused_widget = QApplication.focusWidget()

        if focused_widget:
            widget_name = focused_widget.objectName() or focused_widget.placeholderText() or "виджет"
            self.focus_status.setText(f"Фокус ввода: на {widget_name}")
            self.log_event(f"Фокус перешел на: {widget_name}")
        else:
            self.focus_status.setText("Фокус ввода: ни на одном виджете")
            self.log_event("Фокус сброшен")

    def show_tab_order(self):
        order = []
        current = self.line_edit1

        for _ in range(10):
            next_widget = current.focusNextChild()
            if next_widget and next_widget not in order:
                order.append(next_widget)
                current = next_widget
            else:
                break

        order_text = " → ".join([w.objectName() or w.placeholderText() or "виджет" for w in order[:5]])
        self.tab_order_label.setText(f"Порядок табуляции: {order_text}")

    def eventFilter(self, obj, event):
        if event.type() == QEvent.FocusIn:
            widget_name = obj.objectName() or obj.placeholderText() or "виджет"
            self.log_event(f"FocusIn: {widget_name}")
        elif event.type() == QEvent.FocusOut:
            widget_name = obj.objectName() or obj.placeholderText() or "виджет"
            self.log_event(f"FocusOut: {widget_name}")

        return super().eventFilter(obj, event)

    def create_hotkeys_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        title = QLabel("2. Назначение клавиш быстрого доступа (Hotkeys)")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        info = QLabel("Горячие клавиши (акселераторы) позволяют выполнять действия\n"
                      "без использования мыши. В PyQt5 используются для QAction или QShortcut.")
        info.setStyleSheet("background-color: #f0f0f0; padding: 10px; border-radius: 5px;")
        layout.addWidget(info)

        self.hotkey_counter = 0
        self.hotkey_label = QLabel("Счетчик: 0")
        self.hotkey_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.hotkey_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.hotkey_label)

        grid = QGridLayout()

        btn1 = QPushButton("Увеличить (Ctrl+I)")
        btn1.clicked.connect(self.increment_counter)

        btn2 = QPushButton("Уменьшить (Ctrl+D)")
        btn2.clicked.connect(self.decrement_counter)

        btn3 = QPushButton("Сбросить (Ctrl+R)")
        btn3.clicked.connect(self.reset_counter)

        btn4 = QPushButton("Сохранить (Ctrl+S)")
        btn4.clicked.connect(self.save_counter)

        btn5 = QPushButton("Загрузить (Ctrl+L)")
        btn5.clicked.connect(self.load_counter)

        btn6 = QPushButton("Выход (Ctrl+Q)")
        btn6.clicked.connect(self.exit_app)

        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 1, 0)
        grid.addWidget(btn4, 1, 1)
        grid.addWidget(btn5, 2, 0)
        grid.addWidget(btn6, 2, 1)

        layout.addLayout(grid)

        shortcut_grid = QGridLayout()

        shortcut1 = QShortcut(QKeySequence("F1"), self)
        shortcut1.activated.connect(lambda: self.shortcut_action("F1 - Справка"))

        shortcut2 = QShortcut(QKeySequence("F2"), self)
        shortcut2.activated.connect(lambda: self.shortcut_action("F2 - Быстрое сохранение"))

        shortcut3 = QShortcut(QKeySequence("F5"), self)
        shortcut3.activated.connect(lambda: self.shortcut_action("F5 - Обновить"))

        shortcut4 = QShortcut(QKeySequence("Ctrl+Shift+S"), self)
        shortcut4.activated.connect(lambda: self.shortcut_action("Ctrl+Shift+S - Сохранить как"))

        shortcut5 = QShortcut(QKeySequence("Alt+Enter"), self)
        shortcut5.activated.connect(lambda: self.shortcut_action("Alt+Enter - Полный экран"))

        shortcut6 = QShortcut(QKeySequence("Esc"), self)
        shortcut6.activated.connect(lambda: self.shortcut_action("Esc - Отмена"))

        shortcut_grid.addWidget(QLabel("F1 - Справка"), 0, 0)
        shortcut_grid.addWidget(QLabel("F2 - Быстрое сохранение"), 0, 1)
        shortcut_grid.addWidget(QLabel("F5 - Обновить"), 1, 0)
        shortcut_grid.addWidget(QLabel("Ctrl+Shift+S - Сохранить как"), 1, 1)
        shortcut_grid.addWidget(QLabel("Alt+Enter - Полный экран"), 2, 0)
        shortcut_grid.addWidget(QLabel("Esc - Отмена"), 2, 1)

        layout.addLayout(shortcut_grid)

        self.hotkey_info = QLabel("")
        layout.addWidget(self.hotkey_info)

        self.setup_menu_bar()

        self.tab_widget.addTab(tab, "2. Горячие клавиши")

    def setup_menu_bar(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("&Файл")

        new_action = QAction("&Новый", self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(lambda: self.menu_action("Создать новый файл"))
        file_menu.addAction(new_action)

        open_action = QAction("&Открыть...", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(lambda: self.menu_action("Открыть файл"))
        file_menu.addAction(open_action)

        save_action = QAction("&Сохранить", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(lambda: self.menu_action("Сохранить файл"))
        file_menu.addAction(save_action)

        file_menu.addSeparator()

        exit_action = QAction("&Выход", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        edit_menu = menubar.addMenu("&Правка")

        copy_action = QAction("&Копировать", self)
        copy_action.setShortcut("Ctrl+C")
        copy_action.triggered.connect(lambda: self.menu_action("Копировать"))
        edit_menu.addAction(copy_action)

        paste_action = QAction("&Вставить", self)
        paste_action.setShortcut("Ctrl+V")
        paste_action.triggered.connect(lambda: self.menu_action("Вставить"))
        edit_menu.addAction(paste_action)

        help_menu = menubar.addMenu("&Справка")

        about_action = QAction("&О программе", self)
        about_action.setShortcut("F1")
        about_action.triggered.connect(lambda: self.menu_action("О программе"))
        help_menu.addAction(about_action)

    def increment_counter(self):
        self.hotkey_counter += 1
        self.update_hotkey_display()
        self.log_event(f"Счетчик увеличен: {self.hotkey_counter}")

    def decrement_counter(self):
        self.hotkey_counter -= 1
        self.update_hotkey_display()
        self.log_event(f"Счетчик уменьшен: {self.hotkey_counter}")

    def reset_counter(self):
        self.hotkey_counter = 0
        self.update_hotkey_display()
        self.log_event("Счетчик сброшен")

    def save_counter(self):
        self.hotkey_info.setText(f"Счетчик сохранен: {self.hotkey_counter}")
        self.log_event(f"Сохранение счетчика: {self.hotkey_counter}")

    def load_counter(self):
        self.hotkey_info.setText(f"Счетчик загружен: {self.hotkey_counter}")
        self.log_event(f"Загрузка счетчика: {self.hotkey_counter}")

    def exit_app(self):
        self.log_event("Выход из приложения")
        self.close()

    def update_hotkey_display(self):
        self.hotkey_label.setText(f"Счетчик: {self.hotkey_counter}")

    def shortcut_action(self, action_name):
        self.hotkey_info.setText(f"Выполнено: {action_name}")
        self.log_event(f"Горячая клавиша: {action_name}")

    def menu_action(self, action_name):
        self.hotkey_info.setText(f"Меню: {action_name}")
        self.log_event(f"Действие меню: {action_name}")

    def create_key_events_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        title = QLabel("2. Обработка событий клавиатуры")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        info = QLabel("Основные события клавиатуры:\n"
                      "• keyPressEvent() - нажатие клавиши\n"
                      "• keyReleaseEvent() - отпускание клавиши\n"
                      "• Можно перехватывать любые клавиши")
        info.setStyleSheet("background-color: #f0f0f0; padding: 10px; border-radius: 5px;")
        layout.addWidget(info)

        self.key_display = QLabel("Нажмите любую клавишу...")
        self.key_display.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            background-color: #e3f2fd;
            border: 2px solid #2196F3;
            border-radius: 10px;
            padding: 20px;
            min-height: 60px;
        """)
        self.key_display.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.key_display)

        grid = QGridLayout()

        self.ctrl_pressed = False
        self.alt_pressed = False
        self.shift_pressed = False

        self.ctrl_label = QLabel("Ctrl: НЕТ")
        self.ctrl_label.setStyleSheet("font-size: 14px;")

        self.alt_label = QLabel("Alt: НЕТ")
        self.alt_label.setStyleSheet("font-size: 14px;")

        self.shift_label = QLabel("Shift: НЕТ")
        self.shift_label.setStyleSheet("font-size: 14px;")

        grid.addWidget(self.ctrl_label, 0, 0)
        grid.addWidget(self.alt_label, 0, 1)
        grid.addWidget(self.shift_label, 0, 2)

        layout.addLayout(grid)

        self.last_keys = []
        self.key_history = QTextEdit()
        self.key_history.setReadOnly(True)
        self.key_history.setMaximumHeight(150)
        layout.addWidget(QLabel("История нажатий:"))
        layout.addWidget(self.key_history)


        self.tab_widget.addTab(tab, "2. События клавиш")

    def keyPressEvent(self, event):
        key = event.key()
        text = event.text()
        modifiers = event.modifiers()

        self.ctrl_pressed = modifiers & Qt.ControlModifier
        self.alt_pressed = modifiers & Qt.AltModifier
        self.shift_pressed = modifiers & Qt.ShiftModifier

        key_name = self.get_key_name(key)

        if text and text.isprintable():
            display_text = f"Клавиша: '{text}' ({key_name})"
        else:
            display_text = f"Клавиша: {key_name}"

        if self.ctrl_pressed:
            display_text += " + Ctrl"
        if self.alt_pressed:
            display_text += " + Alt"
        if self.shift_pressed:
            display_text += " + Shift"

        self.key_display.setText(display_text)

        self.ctrl_label.setText(f"Ctrl: {'ДА' if self.ctrl_pressed else 'НЕТ'}")
        self.alt_label.setText(f"Alt: {'ДА' if self.alt_pressed else 'НЕТ'}")
        self.shift_label.setText(f"Shift: {'ДА' if self.shift_pressed else 'НЕТ'}")

        self.last_keys.append((key_name, text, self.ctrl_pressed, self.alt_pressed, self.shift_pressed))
        if len(self.last_keys) > 10:
            self.last_keys.pop(0)

        self.log_event(f"KeyPress: {display_text}")

        if event.key() == Qt.Key_Escape:
            self.key_display.setText("Нажата клавиша ESC")
        elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.key_history.append("--- Enter ---")
        elif event.key() == Qt.Key_Backspace:
            self.key_history.append("--- Backspace ---")
        elif event.key() == Qt.Key_Delete:
            self.key_history.append("--- Delete ---")
        elif event.key() == Qt.Key_Tab:
            self.key_history.append("--- Tab ---")
        elif text and text.isprintable():
            self.key_history.append(f"'{text}'")

        if key == Qt.Key_F11:
            if self.isFullScreen():
                self.showNormal()
            else:
                self.showFullScreen()

        super().keyPressEvent(event)

    def keyReleaseEvent(self, event):
        key = event.key()

        if key == Qt.Key_Control:
            self.ctrl_pressed = False
            self.ctrl_label.setText("Ctrl: НЕТ")
        elif key == Qt.Key_Alt:
            self.alt_pressed = False
            self.alt_label.setText("Alt: НЕТ")
        elif key == Qt.Key_Shift:
            self.shift_pressed = False
            self.shift_label.setText("Shift: НЕТ")

        self.log_event(f"KeyRelease: {self.get_key_name(key)}")
        super().keyReleaseEvent(event)

    def get_key_name(self, key):
        if key >= Qt.Key_A and key <= Qt.Key_Z:
            return chr(key)
        elif key >= Qt.Key_0 and key <= Qt.Key_9:
            return chr(key)

        key_names = {
            Qt.Key_Escape: "Escape",
            Qt.Key_Tab: "Tab",
            Qt.Key_Backspace: "Backspace",
            Qt.Key_Return: "Enter",
            Qt.Key_Enter: "Enter",
            Qt.Key_Insert: "Insert",
            Qt.Key_Delete: "Delete",
            Qt.Key_Pause: "Pause",
            Qt.Key_Print: "Print",
            Qt.Key_SysReq: "SysReq",
            Qt.Key_Clear: "Clear",
            Qt.Key_Home: "Home",
            Qt.Key_End: "End",
            Qt.Key_Left: "Left",
            Qt.Key_Up: "Up",
            Qt.Key_Right: "Right",
            Qt.Key_Down: "Down",
            Qt.Key_PageUp: "PageUp",
            Qt.Key_PageDown: "PageDown",
            Qt.Key_Shift: "Shift",
            Qt.Key_Control: "Control",
            Qt.Key_Meta: "Meta",
            Qt.Key_Alt: "Alt",
            Qt.Key_AltGr: "AltGr",
            Qt.Key_CapsLock: "CapsLock",
            Qt.Key_NumLock: "NumLock",
            Qt.Key_ScrollLock: "ScrollLock",
            Qt.Key_F1: "F1",
            Qt.Key_F2: "F2",
            Qt.Key_F3: "F3",
            Qt.Key_F4: "F4",
            Qt.Key_F5: "F5",
            Qt.Key_F6: "F6",
            Qt.Key_F7: "F7",
            Qt.Key_F8: "F8",
            Qt.Key_F9: "F9",
            Qt.Key_F10: "F10",
            Qt.Key_F11: "F11",
            Qt.Key_F12: "F12",
            Qt.Key_F13: "F13",
            Qt.Key_F14: "F14",
            Qt.Key_F15: "F15",
            Qt.Key_F16: "F16",
            Qt.Key_F17: "F17",
            Qt.Key_F18: "F18",
            Qt.Key_F19: "F19",
            Qt.Key_F20: "F20",
            Qt.Key_F21: "F21",
            Qt.Key_F22: "F22",
            Qt.Key_F23: "F23",
            Qt.Key_F24: "F24",
            Qt.Key_F25: "F25",
            Qt.Key_F26: "F26",
            Qt.Key_F27: "F27",
            Qt.Key_F28: "F28",
            Qt.Key_F29: "F29",
            Qt.Key_F30: "F30",
            Qt.Key_F31: "F31",
            Qt.Key_F32: "F32",
            Qt.Key_F33: "F33",
            Qt.Key_F34: "F34",
            Qt.Key_F35: "F35",
            Qt.Key_Super_L: "Super_L",
            Qt.Key_Super_R: "Super_R",
            Qt.Key_Menu: "Menu",
            Qt.Key_Hyper_L: "Hyper_L",
            Qt.Key_Hyper_R: "Hyper_R",
            Qt.Key_Help: "Help",
            Qt.Key_Direction_L: "Direction_L",
            Qt.Key_Direction_R: "Direction_R",
            Qt.Key_Space: "Space",
            Qt.Key_Exclam: "!",
            Qt.Key_QuoteDbl: "\"",
            Qt.Key_NumberSign: "#",
            Qt.Key_Dollar: "$",
            Qt.Key_Percent: "%",
            Qt.Key_Ampersand: "&",
            Qt.Key_Apostrophe: "'",
            Qt.Key_ParenLeft: "(",
            Qt.Key_ParenRight: ")",
            Qt.Key_Asterisk: "*",
            Qt.Key_Plus: "+",
            Qt.Key_Comma: ",",
            Qt.Key_Minus: "-",
            Qt.Key_Period: ".",
            Qt.Key_Slash: "/",
            Qt.Key_Colon: ":",
            Qt.Key_Semicolon: ";",
            Qt.Key_Less: "<",
            Qt.Key_Equal: "=",
            Qt.Key_Greater: ">",
            Qt.Key_Question: "?",
            Qt.Key_At: "@",
            Qt.Key_BracketLeft: "[",
            Qt.Key_Backslash: "\\",
            Qt.Key_BracketRight: "]",
            Qt.Key_AsciiCircum: "^",
            Qt.Key_Underscore: "_",
            Qt.Key_QuoteLeft: "`",
            Qt.Key_BraceLeft: "{",
            Qt.Key_Bar: "|",
            Qt.Key_BraceRight: "}",
            Qt.Key_AsciiTilde: "~"
        }

        return key_names.get(key, f"Key_{key}")

    def closeEvent(self, event):
        self.log_event("Приложение закрывается")
        super().closeEvent(event)


def main():
    app = QApplication(sys.argv)

    app.setStyle("Fusion")

    window = MainWindow()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()