# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(598, 486)
        self.tableWidget = QtWidgets.QTableWidget(parent=Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 591, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.button_add = QtWidgets.QPushButton(parent=Form)
        self.button_add.setGeometry(QtCore.QRect(40, 430, 121, 41))
        self.button_add.setObjectName("button_add")
        self.button_delete = QtWidgets.QPushButton(parent=Form)
        self.button_delete.setGeometry(QtCore.QRect(210, 420, 191, 51))
        self.button_delete.setObjectName("button_delete")
        self.button_edit = QtWidgets.QPushButton(parent=Form)
        self.button_edit.setGeometry(QtCore.QRect(440, 430, 141, 41))
        self.button_edit.setObjectName("button_edit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button_add.setText(_translate("Form", "Добавить"))
        self.button_delete.setText(_translate("Form", "Удалить"))
        self.button_edit.setText(_translate("Form", "Изменить"))