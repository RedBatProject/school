import sys
from PyQt5 import QtWidgets
 
 
class TestWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(TestWindow, self).__init__(parent=parent)
        self.resize(640, 480)
 
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
 
        widget1 = CustomWidget("One")
        widget2 = CustomWidget("Two")
 
        widget1.layout().addWidget(widget2)
        layout.addWidget(widget1)
 
 
class CustomWidget(QtWidgets.QFrame):
    def __init__(self, name, parent=None):
        super(CustomWidget, self).__init__(parent=parent)
        self.setObjectName(name)
        self.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(QtWidgets.QLabel(name, parent=self))
 
    def enterEvent(self, event):
        print("Enter:", self.objectName())
 
    def leaveEvent(self, event):
        print("Leave:", self.objectName())

if __name__ == "__main__":
    qApp = QtWidgets.QApplication(sys.argv)
    tw = TestWindow()
    tw.show()
    sys.exit(qApp.exec_())