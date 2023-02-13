from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from pytube import YouTube
from mainPage import Ui_MainWindow
from PyQt5 import QtWidgets
class Window(Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.setMainWindow()

    def setMainWindow(self):
        self.setWindowTitle("Berke Karaduman - Youtube Downloader")
        self.setGeometry(250,250,600,80)
        self.youtubeLinkLine.setPlaceholderText("https://www.youtube.com/")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())