

# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QMainWindow ,QSizePolicy
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtGui import QCursor
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from bs4 import BeautifulSoup
# import requests
# from PIL import Image
# from io import BytesIO
# import os
# from zipfile import ZipFile
# from os.path import basename
# from PyQt5 import QtCore, QtGui, QtWidgets
# import jdatetime
# import json
# import sys


# class Ui_MainWindow(QtWidgets.QWidget):
#   def setupUi(self, MainWindow):
#     MainWindow.setObjectName("MainWindow")
#     MainWindow.setFixedSize(1200,720)
#     self.centralwidget = QtWidgets.QWidget(MainWindow)
#     self.centralwidget.setObjectName("centralwidget")
#     MainWindow.setCentralWidget(self.centralwidget)
#     self.retranslateUi(MainWindow)

#     QtCore.QMetaObject.connectSlotsByName(MainWindow)

#   def retranslateUi(self, MainWindow):
#     _translate = QtCore.QCoreApplication.translate
#     # MainWindow.setWindowTitle(_translate("MainWindow", "حضور و غیاب"))
#     self.Question = QtWidgets.QInputDialog()
#     # Question.windowOpacity(1.4)
#     self.Question.setStyleSheet('''*{
#       color : 'red'
#     }''')
#     in_pass, done = self.Question.getText(
#       self, ' ', 'لطفا کد خود را وارد کنید\nدر صورت نداشتن کد عدد 1 را وارد کنید.')
#     try:
#       if not done:
#         # sys.exit(app.exec_())

#         self.destroy()
#         # MainWindow.resize(187, 43)
#         # MainWindow.setWindowTitle(_translate("MainWindow", "ورود به عنوان میهمان"))
#       else:
#         if in_pass=="":
#           MainWindow.setWindowTitle("ورود به عنوان میهمان")
#         elif int(in_pass)==99042:
#           MainWindow.setWindowTitle("ورود به عنوان ادمین")
#     except:
#       pass
#       # QMessageBox.information(self," ", "متاسفانه اجازه‌ی ورود ندارید.")
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()

#     sys.exit(app.exec_())


import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 140))    
        self.setWindowTitle("PyQt Line Edit example (textfield) - pythonprogramminglanguage.com") 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')
        self.line = QLineEdit(self)
        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 60)  
        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)
        self.line.returnPressed.connect(pybutton.click)

    ss = ""
    def clickMethod(self):
        # global ss
        ss = self.line.text()
        self.line.clear()
        print(ss)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )