# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\boobit_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from summary import summary_voulme
import os

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 191)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 61))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonSourceSelect = QtWidgets.QPushButton(Dialog)
        self.buttonSourceSelect.setGeometry(QtCore.QRect(20, 20, 131, 23))
        self.buttonSourceSelect.setObjectName("buttonSourceSelect")
        self.buttonSourceSelect.clicked.connect(self.clickSelectSoruce)
        self.labelSorucePath = QtWidgets.QLabel(Dialog)
        self.labelSorucePath.setGeometry(QtCore.QRect(20, 60, 261, 16))
        self.labelSorucePath.setObjectName("labelSorucePath")
        self.buttonTargetSelect = QtWidgets.QPushButton(Dialog)
        self.buttonTargetSelect.setGeometry(QtCore.QRect(20, 90, 151, 23))
        self.buttonTargetSelect.setObjectName("buttonTargetSelect")
        self.buttonTargetSelect.clicked.connect(self.clickSelectTarget)
        self.labelTargatPath = QtWidgets.QLabel(Dialog)
        self.labelTargatPath.setGeometry(QtCore.QRect(20, 130, 271, 16))
        self.labelTargatPath.setObjectName("labelTargatPath")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Boobit Ref Volume Summary"))
        self.buttonSourceSelect.setText(_translate("Dialog", "Select Source File"))
        self.labelSorucePath.setText(_translate("Dialog", "..."))
        self.buttonTargetSelect.setText(_translate("Dialog", "Select Target Excel File"))
        self.labelTargatPath.setText(_translate("Dialog", "..."))

    def clickSelectSoruce(self, Button):
        self.labelSorucePath.clear()
        dialog = QtWidgets.QFileDialog(Dialog)
        dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        dialog.setNameFilter("CSV (*.csv)")
        if dialog.exec():
            self.labelSorucePath.setText(dialog.selectedFiles()[0])
            print(dialog.selectedFiles())

    def clickSelectTarget(self, Button):
        self.labelTargatPath.clear()
        dialog = QtWidgets.QFileDialog(Dialog)
        dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        dialog.AcceptMode(QtWidgets.QFileDialog.AcceptSave)
        dialog.setNameFilter("Excel (*.xlsx)")
        if dialog.exec():
            self.labelTargatPath.setText(dialog.selectedFiles()[0])
            print(dialog.selectedFiles())

    def accept(self):
        source_path = self.labelSorucePath.text()
        target_path = self.labelTargatPath.text()

        if len(source_path) < 4 or len(target_path) < 4:
            Dialog.reject()
            return

        if os.path.exists(source_path):
            summary_voulme(source_path, target_path)

        Dialog.accept()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
