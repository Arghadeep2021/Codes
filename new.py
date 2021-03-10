import sys

import cv2
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.uic.properties import QtCore


class Project(QMainWindow):
    def __init__(self):
        super(Project,self).__init__()
        loadUi('gen.ui',self)
    #     self.image = None
    #     self.pushButton.clicked.connect(self.loadclicked)
    #
    # def loadclicked(self):
    #     self.loadImage('images.jpeg')
    #
    # def loadImage(self,fname):
    #     self.image = cv2.imread(fname)
    #     self.displayimage()
    #
    # def displayimage(self):
    #     qformat = QImage.Format_Indexed8
    #
    #     if len(self.image.shape)==3:
    #         if (self.image.shape[2])==4:
    #             qformat=QImage.Format_RGB888
    #         else:
    #             qformat=QImage.Format_RGB888
    #         img = QImage(self.image,self.image.shape[1],self.image.shape[0],self.image.strides[0],qformat)
    #
    #         img = img.rgbSwapped()
    #         self.imgLabel.setPixmap(QPixmap.fromimage(img))
    #         self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter)



app = QApplication(sys.argv)
win = Project()
win.show()
sys.exit(app.exec_())