import resource
import sys
import os
import webbrowser
import pyautogui as py


from PyQt5 import QtWidgets,uic

class mainwindow(QtWidgets.QMainWindow):

    def __init__(self):
        
        super(mainwindow, self).__init__()
        
        uic.loadUi('baymax-for-medi.ui', self)
        
        self.button1 = self.findChild(QtWidgets.QPushButton,'feverButton')
        self.button2 = self.findChild(QtWidgets.QPushButton,'headacheButton')
        self.button3 = self.findChild(QtWidgets.QPushButton,'diarrheaButton')
        self.button4 = self.findChild(QtWidgets.QPushButton,'vomitButton')
        self.button5 = self.findChild(QtWidgets.QPushButton,'coldButton')
        self.button6 = self.findChild(QtWidgets.QPushButton,'injuryButton')
        self.button7 = self.findChild(QtWidgets.QPushButton,'allergyButton')
        self.button8 = self.findChild(QtWidgets.QPushButton,'unknownButton')
        self.button9 = self.findChild(QtWidgets.QPushButton,'exitButton')
        
        
        self.button1.clicked.connect(self.fever)
        self.button2.clicked.connect(self.headache)
        self.button3.clicked.connect(self.diarrhea)
        self.button4.clicked.connect(self.vomit)
        self.button5.clicked.connect(self.cold)
        self.button6.clicked.connect(self.injury)
        self.button7.clicked.connect(self.allergy)
        self.button8.clicked.connect(self.unknown)
        self.button9.clicked.connect(self.exit)
   
        
        self.show()

    def fever(self):
        print('fever')
        os.system('mpg321 fever.mp3')
        webbrowser.open_new_tab("https://www.healthline.com/health/effective-fever-remedies#4.-Sleep,-Sleep,-and-More-Sleep")
        return 0

    def headache(self):
        print('head-ache')
        return 0

    def diarrhea(self):
        print('diarrhea')
        return 0
    
    def vomit(self):
        print('vomit')
        return 0
    
    def cold(self):
        print('cold')
        return 0

    def injury(self):
        print('injury')
        return 0

    def allergy(self):
        print('allergy')
        return 0

    def unknown(self):
        print('unknown')
        return 0    

    def exit(self):
        exit()
           




    
def dis_ui():
    app=QtWidgets.QApplication(sys.argv)
    ui=mainwindow()
    app.exec_()

dis_ui()
