from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import sys
import time
import threading
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)



class Thread(QtWidgets.QMainWindow):      #First we make class for main window.

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi('blank.ui',self)
        self.resize(800,300)
        icon = QtGui.QIcon()

        self.setWindowIcon(icon)
        self.pushButton.clicked.connect(self.animate)

    def animate(i):
        graph_data = open('edit.txt', 'r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                xs.append(float(x))
                ys.append(float(y))
        ax1.clear()
        ax1.plot(xs, ys)

    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Thread()
    MainWindow.show()
    sys.exit(app.exec_())
