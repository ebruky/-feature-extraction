# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 12:51:22 2020

@author: ebruk
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from f_code1 import MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
