import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QCalendarWidget

class CalendarApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Календарь")
        self.setGeometry(100, 100, 400, 300)
        layout = QVBoxLayout()

        self.calendar = QCalendarWidget(self)
        self.dlabel = QLabel("Выберите дату:", self)
        self.calendar.clicked.connect(self.show_date)

        layout.addWidget(self.calendar)
        layout.addWidget(self.dlabel)
        self.setLayout(layout)

    def show_date(self, date):
        formd = date.toString("dd.MM.yyyy")
        self.dlabel.setText(f"Выбранная дата: {formd}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalendarApp()
    window.show()
    sys.exit(app.exec_())
