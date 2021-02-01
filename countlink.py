from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import sys
import time
import threading
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Thread(QtWidgets.QMainWindow):      #First we make class for main window.
    counter = pyqtSignal(str)
    counting = False


    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi('count.ui',self)
        self.resize(800,300)
        icon = QtGui.QIcon()

        self.setWindowIcon(icon)
        self.pushButton.clicked.connect(self.startCounting)

        app.aboutToQuit.connect(self.closeEvent)

    def startCounting(self):
        if not self.counting:
            self.counting = True
            thread = threading.Thread(target=self.main)
            thread.start()

    def main(self):
        for x in range(100):
            self.counter.emit(str(x))
            print(x)
            time.sleep(1)
        self.counting = False

    def closeEvent(self):
        #print("User has clicked the red x on the main window")
        #event.accept()
        sys.exit(0)



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Thread()
    MainWindow.show()
    sys.exit(app.exec_())