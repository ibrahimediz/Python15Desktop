from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit
from PyQt5 import uic
import cv2
from PyQt5.QtGui import QImage,QPixmap

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.win = uic.loadUi("kamera.ui")

    def KameraAc(self):
        cam = cv2.VideoCapture(0)
        while 1:
            ret,frame = cam.read()
            buyumeFaktor = 0.8
            frame = cv2.resize(frame,None,fx=buyumeFaktor,
            fy=buyumeFaktor,interpolation=cv2.INTER_AREA)

            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            height,width,channel = frame.shape



            qImg = QImage(frame.data,)