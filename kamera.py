from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit
from PyQt5 import uic
from PyQt5.QtCore import QTimer
import cv2
from PyQt5.QtGui import QImage,QPixmap

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.win = uic.loadUi("kamera.ui")
        self.timer = QTimer()
        self.win.btKamera.clicked.connect(self.btClick)
        self.win.show()

    def btClick(self):
        if not self.timer.isActive():
            self.cam = cv2.VideoCapture(0)
            self.timer.start(3)
            self.KameraAc()
        else:
            self.cam.release()
            self.timer.stop()

        

    def KameraAc(self):
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
        while 1:
            ret,frame = self.cam.read()
            buyumeFaktor = 0.5
            frame = cv2.resize(frame,None,fx=buyumeFaktor,
            fy=buyumeFaktor,interpolation=cv2.INTER_AREA)
            
            #######################Tespit Etme##############################
            gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gri,1.3,5)

            for (x,y,w,h) in faces:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                    roi_gray = gri[y:y+h,x:x+w]
                    roi_color = frame[y:y+h,x:x+w]
                    eyes = eye_cascade.detectMultiScale(roi_gray)
                    for (ex,ey,ew,eh) in eyes:
                            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
            ###################################################################

            ############Yansıtma###################################
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            height,width,channel = frame.shape
            step = channel*width
            qImg = QImage(frame.data,width,height,step,QImage.Format_RGB888)
            self.win.kamera.setPixmap(QPixmap.fromImage(qImg))
            ####################################################
            k = cv2.waitKey(100) & 0xFF
            if k == 27:
                break

        self.cam.release()
        self.timer.stop()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())