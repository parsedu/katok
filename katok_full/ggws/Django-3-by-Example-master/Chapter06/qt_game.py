import sys
import random
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class MathQuiz(QMainWindow):
    def __init__(self):
        super().__init__()

        # Константы
        self.numberTried = 0
        self.numberCorrect = 0
        self.correctAnswer = 0
        self.problem = ""
        self.yourAnswer = ""
        self.numberDigits = 1
        self.problemTime = 0
        self.problemTimer = QTimer()

        # ИНИЦИАЛИЗИРУЕМ ВСЕ СПИСКИ ЗАРАНЕЕ
        self.typeCheckBox = []
        self.factorRadioButton = []
        self.timerRadioButton = []

        self.initUI()
        self.setupTimers()

    def initUI(self):
        self.setWindowTitle("Математическая викторина")
        self.setFixedSize(650, 550)
        self.setStyleSheet("background-color: #ffffc0;")

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QGridLayout(central_widget)

        # Шрифт
        myFont = QFont("Arial", 18)

        # ===== ВЕРХНЯЯ ЧАСТЬ: Попытки и правильные ответы =====
        triedLabel = QLabel("Попытки:")
        triedLabel.setFont(myFont)
        layout.addWidget(triedLabel, 0, 0, Qt.AlignmentFlag.AlignLeft)

        self.triedTextField = QLineEdit("0")
        self.triedTextField.setFixedSize(90, 30)
        self.triedTextField.setReadOnly(True)
        self.triedTextField.setStyleSheet("background-color: red; color: yellow;")
        self.triedTextField.setFont(myFont)
        self.triedTextField.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.triedTextField, 0, 1, Qt.AlignmentFlag.AlignLeft)

        correctLabel = QLabel("Правильно:")
        correctLabel.setFont(myFont)
        layout.addWidget(correctLabel, 0, 2, Qt.AlignmentFlag.AlignLeft)

        self.correctTextField = QLineEdit("0")
        self.correctTextField.setFixedSize(90, 30)
        self.correctTextField.setReadOnly(True)
        self.correctTextField.setStyleSheet("background-color: red; color: yellow;")
        self.correctTextField.setFont(myFont)
        self.correctTextField.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.correctTextField, 0, 3, Qt.AlignmentFlag.AlignLeft)

        # ===== ПРОБЛЕМА (пример) =====
        self.problemLabel = QLabel()
        self.problemLabel.setFont(QFont("Arial", 24))
        self.problemLabel.setFixedHeight(50)
        self.problemLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.problemLabel.setStyleSheet("border: 2px solid black; background-color: white;")
        self.problemLabel.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        layout.addWidget(self.problemLabel, 1, 0, 1, 5)

        # ===== РАЗДЕЛИТЕЛЬ =====
        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.HLine)
        divider.setStyleSheet("background-color: red; height: 5px;")
        divider.setFixedHeight(5)
        layout.addWidget(divider, 2, 0, 1, 5)

        # ===== ПАНЕЛЬ ТИПОВ (Сложение, Вычитание и т.д.) =====
        typePanel = QGroupBox("Тип:")
        typePanel.setFixedSize(180, 150)
        typePanel.setStyleSheet("background-color: #c0c0ff;")
        typeLayout = QVBoxLayout(typePanel)

        typeNames = ["Сложение", "Вычитание", "Умножение", "Деление"]
        for i, name in enumerate(typeNames):
            cb = QCheckBox(name)
            cb.setStyleSheet("background-color: #c0c0ff;")
            # Используем замыкание с фиксацией значения i
            cb.toggled.connect(lambda checked, idx=i: self.typeCheckBoxActionPerformed(idx))
            typeLayout.addWidget(cb)
            self.typeCheckBox.append(cb)

        self.typeCheckBox[0].setChecked(True)  # По умолчанию сложение

        layout.addWidget(typePanel, 3, 0, 1, 2, Qt.AlignmentFlag.AlignTop)

        # ===== ПАНЕЛЬ МНОЖИТЕЛЕЙ =====
        factorPanel = QGroupBox("Множитель:")
        factorPanel.setFixedSize(180, 200)
        factorPanel.setStyleSheet("background-color: #c0c0ff;")
        factorLayout = QGridLayout(factorPanel)

        self.factorButtonGroup = QButtonGroup()

        x, y = 0, 0
        for i in range(11):
            rb = QRadioButton(str(i))
            rb.setStyleSheet("background-color: #c0c0ff;")
            self.factorButtonGroup.addButton(rb)
            factorLayout.addWidget(rb, y, x, Qt.AlignmentFlag.AlignLeft)
            self.factorRadioButton.append(rb)

            x += 1
            if x > 2:
                x = 0
                y += 1

        # Случайный множитель (10)
        self.factorRadioButton[10].setText("Случайный")
        self.factorRadioButton[10].setChecked(True)

        layout.addWidget(factorPanel, 3, 2, 1, 1, Qt.AlignmentFlag.AlignTop)

        # ===== ПАНЕЛЬ ТАЙМЕРА =====
        timerPanel = QGroupBox("Секундомер:")
        timerPanel.setFixedSize(200, 180)
        timerPanel.setStyleSheet("background-color: #c0c0ff;")
        timerLayout = QGridLayout(timerPanel)

        self.timerButtonGroup = QButtonGroup()
        timerNames = ["Выключить", "Прямой отсчет", "Обратный отсчет"]

        for i, name in enumerate(timerNames):
            rb = QRadioButton(name)
            rb.setStyleSheet("background-color: #c0c0ff;")
            rb.toggled.connect(self.timerRadioButtonActionPerformed)
            self.timerButtonGroup.addButton(rb)
            timerLayout.addWidget(rb, i, 0, 1, 2, Qt.AlignmentFlag.AlignLeft)
            self.timerRadioButton.append(rb)

        self.timerRadioButton[0].setChecked(True)

        self.timerTextField = QLineEdit("Выключить")
        self.timerTextField.setFixedSize(120, 25)
        self.timerTextField.setReadOnly(True)
        self.timerTextField.setStyleSheet("background-color: white; color: red;")
        self.timerTextField.setFont(myFont)
        self.timerTextField.setAlignment(Qt.AlignmentFlag.AlignCenter)
        timerLayout.addWidget(self.timerTextField, 3, 0, Qt.AlignmentFlag.AlignLeft)

        self.timerScrollBar = QScrollBar(Qt.Orientation.Vertical)
        self.timerScrollBar.setMinimum(1)
        self.timerScrollBar.setMaximum(60)
        self.timerScrollBar.setValue(1)
        self.timerScrollBar.setEnabled(False)
        self.timerScrollBar.valueChanged.connect(self.timerScrollBarValueChanged)
        timerLayout.addWidget(self.timerScrollBar, 3, 1, Qt.AlignmentFlag.AlignLeft)

        layout.addWidget(timerPanel, 3, 3, 1, 2, Qt.AlignmentFlag.AlignTop)

        # ===== КНОПКИ =====
        buttonLayout = QHBoxLayout()

        self.startButton = QPushButton("Начать")
        self.startButton.clicked.connect(self.startButtonClicked)
        buttonLayout.addWidget(self.startButton)

        self.exitButton = QPushButton("Выход")
        self.exitButton.clicked.connect(self.exitButtonClicked)
        buttonLayout.addWidget(self.exitButton)

        layout.addLayout(buttonLayout, 4, 0, 1, 5)

    def setupTimers(self):
        self.problemTimer.timeout.connect(self.problemTimerAction)

    def keyPressEvent(self, event):
        """Глобальная обработка клавиш"""
        self.problemLabelKeyPressed(event)

    def typeCheckBoxActionPerformed(self, clicked_idx):
        """Обработка выбора типа операции"""
        # Проверяем, что объекты уже созданы
        if not hasattr(self, 'factorRadioButton') or len(self.factorRadioButton) == 0:
            return

        numberOfChecks = sum(1 for cb in self.typeCheckBox if cb.isChecked())

        if numberOfChecks == 0:
            self.typeCheckBox[clicked_idx].setChecked(True)
            return

        if clicked_idx == 3 and self.typeCheckBox[3].isChecked():
            if self.factorRadioButton[0].isChecked():
                self.factorRadioButton[1].setChecked(True)
            self.factorRadioButton[0].setEnabled(False)
        else:
            if not self.factorRadioButton[0].isEnabled():
                self.factorRadioButton[0].setEnabled(True)

        self.problemLabel.setFocus()

    def timerRadioButtonActionPerformed(self):
        """Обработка выбора режима таймера"""
        # Проверяем, что объект уже создан
        if not hasattr(self, 'timerTextField'):
            return

        if self.timerRadioButton[0].isChecked():
            self.timerTextField.setText("Выключить")
            if hasattr(self, 'timerScrollBar'):
                self.timerScrollBar.setEnabled(False)
        elif self.timerRadioButton[1].isChecked():
            self.problemTime = 0
            self.timerTextField.setText(self.getTime(self.problemTime))
            if hasattr(self, 'timerScrollBar'):
                self.timerScrollBar.setEnabled(False)
        elif self.timerRadioButton[2].isChecked():
            if hasattr(self, 'timerScrollBar'):
                self.problemTime = 30 * self.timerScrollBar.value()
                self.timerTextField.setText(self.getTime(self.problemTime))
                self.timerScrollBar.setEnabled(True)

    def timerScrollBarValueChanged(self):
        """Изменение значения скроллбара таймера"""
        if hasattr(self, 'timerTextField') and hasattr(self, 'timerScrollBar'):
            self.problemTime = 30 * self.timerScrollBar.value()
            self.timerTextField.setText(self.getTime(self.problemTime))

    def startButtonClicked(self):
        """Обработка нажатия кнопки Старт/Стоп"""
        if self.startButton.text() == "Начать":
            self.startButton.setText("Остановить")
            self.exitButton.setEnabled(False)
            self.numberTried = 0
            self.numberCorrect = 0
            self.triedTextField.setText("0")
            self.correctTextField.setText("0")

            # Блокируем радио-кнопки таймера
            for rb in self.timerRadioButton:
                rb.setEnabled(False)
            self.timerScrollBar.setEnabled(False)

            # Настройка таймера
            if not self.timerRadioButton[0].isChecked():
                if self.timerRadioButton[1].isChecked():
                    self.problemTime = 0
                else:
                    self.problemTime = 30 * self.timerScrollBar.value()
                    self.timerTextField.setText(self.getTime(self.problemTime))
                    self.problemTimer.start(1000)

            self.problemLabel.setText(self.getProblem())
            self.problemLabel.setFocus()
        else:
            # Разблокируем радио-кнопки
            for rb in self.timerRadioButton:
                rb.setEnabled(True)
            if self.timerRadioButton[2].isChecked():
                self.timerScrollBar.setEnabled(True)

            self.problemTimer.stop()
            self.startButton.setText("Начать")
            self.exitButton.setEnabled(True)
            self.problemLabel.setText("")

            if self.numberTried > 0:
                score = int(100 * self.numberCorrect / self.numberTried)
                message = f"Попыток: {self.numberTried}\n"
                message += f"Правильных: {self.numberCorrect} ({score}%)\n"

                if self.timerRadioButton[0].isChecked():
                    message += "Таймер выключен"
                else:
                    if self.timerRadioButton[2].isChecked():
                        self.problemTime = 30 * self.timerScrollBar.value() - self.problemTime
                    message += f"Прошло времени: {self.getTime(self.problemTime)}\n"
                    message += f"Среднее время на задание: {self.problemTime / self.numberTried:.2f} сек"

                QMessageBox.information(self, "Результаты", message)

    def exitButtonClicked(self):
        """Выход из программы"""
        self.close()

    def getFactor(self, pType):
        """Получение множителя в зависимости от выбора"""
        if self.factorRadioButton[10].isChecked():  # Случайный
            if pType == 4:  # Деление
                return random.randint(2, 9)
            else:
                return random.randint(0, 9)
        else:
            for i, rb in enumerate(self.factorRadioButton):
                if rb.isChecked() and i < 10:
                    return i
        return 1

    def getProblem(self):
        """Генерация нового примера"""
        p = 0
        while p == 0:
            pType = random.randint(1, 4)

            if pType == 1 and self.typeCheckBox[0].isChecked():  # Сложение
                p = pType
                number = random.randint(0, 9)
                factor = self.getFactor(1)
                self.correctAnswer = number + factor
                self.problem = f"{number} + {factor} = "

            elif pType == 2 and self.typeCheckBox[1].isChecked():  # Вычитание
                p = pType
                factor = self.getFactor(2)
                self.correctAnswer = random.randint(0, 9)
                number = self.correctAnswer + factor
                self.problem = f"{number} - {factor} = "

            elif pType == 3 and self.typeCheckBox[2].isChecked():  # Умножение
                p = pType
                number = random.randint(0, 9)
                factor = self.getFactor(3)
                self.correctAnswer = number * factor
                self.problem = f"{number} × {factor} = "

            elif pType == 4 and self.typeCheckBox[3].isChecked():  # Деление
                p = pType
                factor = self.getFactor(4)
                self.correctAnswer = random.randint(0, 9)
                number = self.correctAnswer * factor
                self.problem = f"{number} ÷ {factor} = "

        self.yourAnswer = ""
        self.digitNumber = 0
        return self.problem

    def problemLabelKeyPressed(self, event):
        """Обработка нажатий клавиш на поле задачи"""
        if self.startButton.text() != "Остановить":
            return

        key = event.key()

        if Qt.Key.Key_0 <= key <= Qt.Key.Key_9:
            # Цифра
            digit = chr(event.key())
            self.yourAnswer += digit
            self.problemLabel.setText(self.problem + self.yourAnswer)
            self.digitNumber += 1

        elif key in (Qt.Key.Key_Return, Qt.Key.Key_Enter, Qt.Key.Key_Space):
            # Проверка ответа
            if self.yourAnswer:
                self.numberTried += 1

                try:
                    if int(self.yourAnswer) == self.correctAnswer:
                        self.numberCorrect += 1
                except ValueError:
                    pass

                self.triedTextField.setText(str(self.numberTried))
                self.correctTextField.setText(str(self.numberCorrect))
                self.problemLabel.setText(self.getProblem())

    def problemTimerAction(self):
        """Действие таймера"""
        if self.timerRadioButton[1].isChecked():  # Прямой отсчет
            self.problemTime += 1
            self.timerTextField.setText(self.getTime(self.problemTime))
            if self.problemTime >= 1800:
                self.startButton.click()
                return
        elif self.timerRadioButton[2].isChecked():  # Обратный отсчет
            if self.problemTime > 0:
                self.problemTime -= 1
                self.timerTextField.setText(self.getTime(self.problemTime))
                if self.problemTime <= 0:
                    self.startButton.click()
                    return

    def getTime(self, s):
        """Форматирование времени"""
        minutes = s // 60
        seconds = s % 60
        return f"{minutes}:{seconds:02d}"


def main():
    app = QApplication(sys.argv)
    quiz = MathQuiz()
    quiz.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()