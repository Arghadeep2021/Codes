import sys
import cv2
from PyQt5 import QtCore
from PyQt5.QtGui import QImage , QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5.uic import loadUi


class Gui(QDialog):
    def __init__(self):
        super(Gui,self).__init__()
        loadUi('gui.ui',self)
        self.image = None
        self.pushButton.clicked.connect(self.loadClick)  ##conects to loadclick function

        self.pushButton2.clicked.connect(self.saveFile)  ##conects to saveFile function
        self.pushButton3.clicked.connect(self.Cannyedge) ##connects to Cannyedge function

    def loadClick(self):
        #self.loadImage('download.jpg')

        ## fname and filter takes the QFileDialog to show the pop up and describes the directory and image filters
        fname, filter = QFileDialog.getOpenFileName(self, "Open File", "C:\\","Image Files (*.jpg)")
        if fname:  ##if file name is ok then it gets loaded.   Else error message is showed.
            self.loadImage(fname)

        else:
            print('Error')

    def saveFile(self):
        fname, filter = QFileDialog.getSaveFileName(self, "Save File", "C:\\", "Image File (*.jpg)")
        ## here the getsavefileame saves in the same way like selected.

        if fname:     ## if file name is okay then cv2.imwrite  cv2.imwrite() method
                      ## is used to save an image to any storage device.
                      ## This will save the image according to the specified format in current working directory.
            cv2.imwrite(fname, self.image)

        else:
            print("Invalid Source")



    def loadImage(self,fname):
        self.image = cv2.imread(fname)     ##reads the filename
        self.displayImage(1)

    def Cannyedge(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) if len(self.image.shape)>= 3 else self.image
        self.image = cv2.Canny(gray, 100, 200)
        self.displayImage(2)


    def displayImage(self,window=1):
        qformat = QImage.Format_Indexed8  ## to display a cv image in qt, we need to use the QImage format.


        if len(self.image.shape)==3:   ## self.image.shape returs three things -- rows[0] rows with indexed 0
                                       ## coloums[1] with index 1 and channels[2] with index 2
            if (self.image.shape[2])==4:  ##checking whether it s a 4 channel image or not.
                qformat = QImage.Format_RGBA8888      ##if 4 channels then assign the qformat with rgba8888

            else:
                qformat = QImage.Format_RGB888   ##else if 3 channel then rgb888.

            img = QImage(self.image, self.image.shape[1],self.image.shape[0], self.image.strides[0],qformat)
                    ##here toshow cv image and QImage is for display of image and image.shape[1] is shape
                    ## image.shape[0] is the width and image.strides[0] gives the byte to jump to next item to memory
                    ## from one item to another in a particular direction/array.

            ##In opencv the picture is in bgr format and thus we convert to rgb.
            img = img.rgbSwapped()
            if window==1:
                self.label.setPixmap(QPixmap.fromImage(img))
            #self.label.setPixmap(QPixmap.fromImage(img))     ##we here set the image in label.
                                                            ##QPixmap adjusts the dimensions.
                self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

            if window==2:
                self.label2.setPixmap(QPixmap.fromImage(img))
                self.label2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)






app= QApplication(sys.argv)
window = Gui()
window.show()
sys.exit(app.exec_())
