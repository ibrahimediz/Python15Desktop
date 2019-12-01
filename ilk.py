from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit
from PyQt5 import uic

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win = uic.loadUi(r"GUI\ilk.ui")
        self.win.but1.clicked.connect(self.AlVer)
        self.win.horse1.valueChanged.connect(self.degisim)
        self.win.chck1.clicked.connect(self.degisim2)
        self.win.show()
    
    def degisim(self):
        var1 =  self.win.horse1.value()
        self.win.lbl3.setText(str(var1))

    def degisim2(self):
        if self.win.chck1.isChecked():
            self.win.txt1.setEchoMode(QLineEdit.Normal)
        else:
            self.win.txt1.setEchoMode(QLineEdit.Password)
    def AlVer(self):
        metin = self.win.txt1.text()
        self.win.lbl1.setText(metin)

        if self.win.rdb1.isChecked():
            self.win.lbl4.setText("İşaretli")
        else: 
            self.win.lbl4.setText("")
        
        if self.win.rdb2.isChecked():
            self.win.lbl5.setText("İşaretli")
        else: 
            self.win.lbl5.setText("")

        if self.win.chck1.isChecked():
            self.win.lbl6.setText("İşaretli")
        else: 
            self.win.lbl6.setText("")                    

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())