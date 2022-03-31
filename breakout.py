import sys
import urllib.parse
import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from rich.console import Console  



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(750, 250))    
        self.setWindowTitle("DevOps Group 7") 

        self.location = QLabel(self)
        self.location.setText('Set Specified Location:')
        self.line1 = QLineEdit(self)

        self.line1.move(200, 30)
        self.line1.resize(200, 30)
        self.location.move(20, 30)

        self.destination = QLabel(self)
        self.destination.setText('Set Specified Destination:')
        self.line2 = QLineEdit(self)

        self.line2.move(200, 70)
        self.line2.resize(230, 30)
        self.destination.m        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(150, 110)        

    def clickMethod(self):
        main_api = "https://www.mapquestapi.com/directions/v2/route?"
        key = "ZNHMGB2uNH3ZOXj0RREYyHxu4y6P5ufG"


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
