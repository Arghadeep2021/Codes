from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import sys

class Thread(QtWidgets.QMainWindow):  #First we make class for main window.
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi('thread.ui',self)
        self.resize(300,300,300,300)
        icon = QtGui.QIcon()
        self.setWindowIcon(icon)

        self.thread = {}
        self.pushButton.clicked.connect(self.start_work_1)
        self.pushButton_2.clicked.connect(self.start_work_2)
        self.pushButton_3.clicked.connect(self.start_worker_3)
        self.pushButton_4.clicked.connect(self.stop_worker_1)
        self.pushButton_5.clicked.connect(self.stop_worker_2)
        self.pushButton_6.clicked.connect(self.stop_worker_3)

    def start_worker_1(self):
        self.thread[1]= ThreadClass (parent = None, index = 1) #The function is defined
        self.thread[1]=start()                   #call the ThreadClass and pass index of worker
        self.thread[1].any_signal.connect(self.my_function) #start thread and connect signal to func 'my_func'
        self.pushButton.setEnabled(False)   #once thread starts then we can disable the button

                            #Same for all three start worker.

    def start_worker_2(self):
        self.thread[2]=ThreadClass(parent = None, index = 1)
        self.thread[2]=start()
        self.thread[2].any_signal.connect(self.my_function)
        self.pushButton_2.setEnabled(False)

    def start_worker_3(self):
        self.thread[3]=ThreadClass(parent = None, index = 1)
        self.thread[3]=start()
        self.thread[3].any_signal.connect(self.my_function)
        self.pushButton_3.setEnabled(False)

                    #Now for the stop_worker func if thread is stopped then the button is made to True.

    def stop_worker_1(self):
        self.thread[1]=stop()
        self.pushButton_4.setEnabled(True)  #once thread stops we can start with the start thread pushbutton.


    def stop_worker_2(self):
        self.thread[2]=stop()
        self.pushButton_5.setEnabled(True)


    def stop_worker_3(self):
        self.thread[3]= stop()
        self.pushButton_6.setEnabled(True)


    def my_function(self,counter): #we make my_function with counter as its second parameter.
        cnt = counter
        index = self.sender().index() #self.sender is a threadClass object which has its own index value.
        if index==1:
            self.progressBar.setValue(cnt)
        if index==2:
            self.progressBar_2.setValue(cnt)
        if index==3:
            self.progressBar_3.setvalue(cnt)

class ThreadClass(QtCore.QThread): #make ThreadClass sub class under main class Thread & initialise its signal.
    any_signal = QtCore.pyqtSignal(int)   #Here QThread is the super class.
    def __init__(self, parent = None, index = 0):
        super(ThreadClass,self).__init__(parent)
        self.index =index
        self.is_running = True

    def run(self):
        print("Starting thread", self.index)
        cnt += 1
        if cnt==99 : cnt==0
        time.sleep(0.01)
        self.any_signal.emit(cnt)

    def stop(self):
        self.is_running = False
        print("Threading about to stop", self.index)
        self.terminate()


app = QtWidgets.QApplication(sys.argv)
MainWindow = Thread()
MainWindow.show()
sys.exit(app.exec_())





