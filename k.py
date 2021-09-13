from PyQt5.QtWidgets import QListWidget, QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

import sys


class AnotherWindow(QWidget):

    def __init__(self,name):
        super().__init__()
        self.name = name
        self.listWidget = QListWidget(self)
        # self.label = QLabel(f'{self.name}')
        self.listWidget.addItem(f'{self.name}')
        # self.setLayout(self.listWidget)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(lambda: self.show_new_window(2))
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        # name1= ["s","s"]
        self.checked = checked
        self.w = AnotherWindow(self.checked)
        self.w.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()