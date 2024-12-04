from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
import sqlite3
from PyQt6 import uic
import sys


class Wind(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

        self.update_table()
        self.connectButtons()

    def connectButtons(self):
        self.button_add.clicked.connect(self.add)
        self.button_delete.clicked.connect(self.delete)
        self.button_edit.clicked.connect(self.edit)

    def update_table(self):
        db = sqlite3.connect("coffee.sqlite")
        cursor = db.cursor()
        data = cursor.execute("SELECT * FROM coffee").fetchall()
        self.next_id = data[-1][0] + 1

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))
        self.tableWidget.setHorizontalHeaderLabels(["id", "название", "обжарка", "зёрна/молотый",
                                                    "описание вкуса", "цена в рублях", "объём упаковки"])
        for i, line in enumerate(data):
            for j, item in enumerate(line):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(item)))
        self.tableWidget.resizeColumnsToContents()

        db.close()

    def add(self):
        self.add_window = EditOrAdd(1, parent=self)
        self.add_window.show()

    def delete(self):

        current_id = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()

        valid = QMessageBox.question(self, "", F"Действительно удалить элемент с id {current_id}?",
                                     buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if valid == QMessageBox.StandardButton.Yes:
            db = sqlite3.connect("coffee.sqlite")
            cursor = db.cursor()
            cursor.execute(F"DELETE FROM coffee WHERE id={int(current_id)}")
            db.commit()
            db.close()
            self.update_table()

    def edit(self):
        row, column = self.tableWidget.currentRow(), self.tableWidget.currentColumn()
        item_id = self.tableWidget.item(row, 0).text()

        self.edit_window = EditOrAdd(0, item_id=item_id, parent=self)
        self.edit_window.show()


class EditOrAdd(QWidget):
    def __init__(self, edit_or_add, item_id=None, parent=None):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)

        self.setWindowTitle("edit_or_add")
        self.edit_or_add = edit_or_add  # 1 - add, 0 - edit
        self.item_id = item_id
        self.parent = parent

        if self.edit_or_add == 0:
            db = sqlite3.connect("coffee.sqlite")
            cursor = db.cursor()
            line_data = cursor.execute(F"SELECT * FROM coffee WHERE id={self.item_id}").fetchall()[0]
            self.nameEdit.setText(line_data[1])
            self.roastingEdit.setText(line_data[2])
            self.beansEdit.setCurrentIndex({"Молотый": 0, "В зёрнах": 1}[line_data[3]])
            self.descEdit.setText(line_data[4])
            self.priceEdit.setText(str(line_data[5]))
            self.volumeEdit.setText(str(line_data[6]))

            self.commitButton.clicked.connect(self.edit)
            db.close()

        if self.edit_or_add == 1:
            self.commitButton.clicked.connect(self.add)

    def add(self):
        try:
            datas = [self.nameEdit.text(), self.roastingEdit.text(), self.beansEdit.currentText(), self.descEdit.text(),
                     int(self.priceEdit.text()), int(self.volumeEdit.text())]
            if not all(datas):
                return
            db = sqlite3.connect("coffee.sqlite")
            cursor = db.cursor()
            cursor.execute(F"INSERT INTO coffee VALUES({self.parent.next_id}, '{datas[0]}', '{datas[1]}',"
                           F" '{datas[2]}', '{datas[3]}', {datas[4]}, {datas[5]})")
            db.commit()
            db.close()
            self.parent.update_table()
            self.close()
        except Exception:
            return

    def edit(self):
        try:
            datas = [self.nameEdit.text(), self.roastingEdit.text(), self.beansEdit.currentText(), self.descEdit.text(),
                     int(self.priceEdit.text()), int(self.volumeEdit.text())]
            if not all(datas):
                return
            db = sqlite3.connect("coffee.sqlite")
            cursor = db.cursor()
            cursor.execute(F"UPDATE coffee SET name='{datas[0]}', roasting='{datas[1]}', groundBeans='{datas[2]}',"
                           F" description='{datas[3]}', price={datas[4]}, volume={datas[5]}"
                           F" WHERE id={self.item_id}")
            db.commit()
            db.close()
            self.parent.update_table()
            self.close()
        except Exception:
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Wind()
    ex.show()
    sys.exit(app.exec())
