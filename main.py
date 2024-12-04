from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem
import sqlite3
from PyQt6 import uic
import sys


class Wind(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

        self.update_table()

    def update_table(self):
        db = sqlite3.connect("coffee.sqlite")

        cursor = db.cursor()

        data = cursor.execute("SELECT * FROM coffee").fetchall()

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))
        self.tableWidget.setHorizontalHeaderLabels(["id", "название", "обжарка", "зёрна/молотый",
                                                    "описание вкуса", "цена в рублях", "объём упаковки"])
        for i, line in enumerate(data):
            for j, item in enumerate(line):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(item)))
        self.tableWidget.resizeColumnsToContents()

        db.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Wind()
    ex.show()
    sys.exit(app.exec())
