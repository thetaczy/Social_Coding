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
        self.destination.move(20, 70)

        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(150, 110)        

    def clickMethod(self):
        main_api = "https://www.mapquestapi.com/directions/v2/route?"
        key = "ZNHMGB2uNH3ZOXj0RREYyHxu4y6P5ufG"
        console = Console()

        
        url = main_api + urllib.parse.urlencode({"key":key, "from":self.line1.text(), "to":self.line2.text()})
        console.print("URL: " + (url))
        json_data = requests.get(url).json()
        json_status = json_data["info"]["statuscode"]
        orig = self.line1.text()
        dest = self.line2.text()
        if json_status == 0:
                console.print("API Status: " + str(json_status) + " =[red] A successful route call. \n")
                console.print("===================================================================")
                console.print("[green]Directions from " + (orig) + " to " + (dest))
                console.print("[blue]Trip Duration:   [/]" + (json_data["route"]["formattedTime"]))
                console.print("[blue]Kilometers:      [/]" + str("{:.2f}".format(json_data["route"]["distance"]*1.61)))
                console.print("[blue]Fuel Used (Ltr): [/]" + str("{:.2f}".format(json_data["route"]["fuelUsed"]*3.78)))
                console.print("===================================================================")
                for each in json_data["route"]["legs"][0]["maneuvers"]:
                 console.print("[yellow]" + (each["narrative"]) + " (" + str("{:.2F}".format((each["distance"])*1.61) + " km)"))
                 console.print("===================================================================\n")
        elif json_status == 402:
                console.print("********************************************")
                console.print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
                console.print("**********************************************\n")
        elif json_status == 611:
                console.print("********************************************")
                console.print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
                console.print("**********************************************\n")
        else:
                console.print("**********************************************************************")
                console.print("For Staus Code: " + str(json_status) + "; Refer to:")
                console.print("https://developer.mapquest.com/documentation/directions-api/status-codes")
                console.print("************************************************************************\n")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )