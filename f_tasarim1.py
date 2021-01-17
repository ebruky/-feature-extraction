# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f_tasarim.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(769, 573)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 761, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.data = QtWidgets.QTableWidget(self.tab)
        self.data.setGeometry(QtCore.QRect(20, 30, 331, 461))
        self.data.setObjectName("data")
        self.data.setColumnCount(0)
        self.data.setRowCount(0)
        self.images = QtWidgets.QListWidget(self.tab)
        self.images.setGeometry(QtCore.QRect(430, 40, 256, 192))
        self.images.setObjectName("images")
        self.secilen_img = QtWidgets.QLabel(self.tab)
        self.secilen_img.setGeometry(QtCore.QRect(470, 280, 191, 181))
        self.secilen_img.setObjectName("secilen_img")
        self.verileriYukle = QtWidgets.QPushButton(self.tab)
        self.verileriYukle.setGeometry(QtCore.QRect(140, 10, 75, 23))
        self.verileriYukle.setObjectName("verileriYukle")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.algoritma = QtWidgets.QComboBox(self.tab_2)
        self.algoritma.setGeometry(QtCore.QRect(140, 70, 141, 22))
        self.algoritma.setObjectName("algoritma")
        self.basari = QtWidgets.QLineEdit(self.tab_2)
        self.basari.setGeometry(QtCore.QRect(140, 110, 141, 20))
        self.basari.setObjectName("basari")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(30, 70, 101, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 46, 13))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.secilen_img.setText(_translate("Dialog", "TextLabel"))
        self.verileriYukle.setText(_translate("Dialog", "Verileri Yükle"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Veriseti ve Resimler"))
        self.label.setText(_translate("Dialog", "Seçilen Algoritma:"))
        self.label_2.setText(_translate("Dialog", "Başarı:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Algoritmalar ve Başarıları"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Confusion Matrix "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

