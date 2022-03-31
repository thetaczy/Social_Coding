import sys
import urllib.parse
import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize




class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(400, 200))    
        self.setWindowTitle("Direction Finder") 

        self.location = QLabel(self)
        self.location.setText('Source:')
        self.line1 = QLineEdit(self)

        self.line1.move(150, 30)
        self.line1.resize(200, 30)
        self.location.move(20, 30)

        self.destination = QLabel(self)
        self.destination.setText('Destination:')
        self.line2 = QLineEdit(self)

        self.line2.move(150, 70)
        self.line2.resize(200, 30)
        self.destination.move(20, 70)

        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(150, 110)        

    def clickMethod(self):
        main_api = "https://www.mapquestapi.com/directions/v2/route?"
        key = "tlis8gsbYF4Ue4E6mdibYgdte9YCiYPR"
        

        
        url = main_api + urllib.parse.urlencode({"key":key, "from":self.line1.text(), "to":self.line2.text()})
        print("URL: " + (url))
        json_data = requests.get(url).json()
        json_status = json_data["info"]["statuscode"]
        orig = self.line1.text()
        dest = self.line2.text()
        if json_status == 0:
            print("API Status: " + str(json_status) + " = A successful route call.\n")
            print("=============================================")
            print("Directions from " + (orig) + " to " + (dest))
            print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
            print("Geolocation:   ")
            print(" Lower Right:   " + "Lat: " + str("{:.2f}".format((json_data["route"]["boundingBox"]["lr"]["lng"]))) + " Lng: " + str("{:.2f}".format((json_data["route"]["boundingBox"]["lr"]["lat"]))))
            print(" Upper Left :   " + "Lat: " + str("{:.2f}".format((json_data["route"]["boundingBox"]["ul"]["lng"]))) + " Lng: " + str("{:.2f}".format((json_data["route"]["boundingBox"]["ul"]["lat"]))))
            print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
            print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
            print("=============================================")
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
            print("=============================================\n")
        elif json_status == 402:
            print("**********************************************")
            print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
            print("**********************************************\n")
        elif json_status == 611:
            print("**********************************************")
            print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
            print("**********************************************\n")
        else:
            print("************************************************************************")
            print("For Staus Code: " + str(json_status) + "; Refer to:")
            print("https://developer.mapquest.com/documentation/directions-api/status-codes")
            print("************************************************************************\n")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )