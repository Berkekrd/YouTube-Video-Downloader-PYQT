from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from pytube import YouTube
from mainPage import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject,QThread,pyqtSignal
class Window(Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.setMainWindow()
        self.YoutubeDownloadButon.clicked.connect(self.YoutubeDownloadButonFunction)
        self.youtubeDetailButon.clicked.connect(self.display)
    def setMainWindow(self):
        self.setWindowTitle("Berke Karaduman - Youtube Downloader")
        self.setGeometry(250,250,600,80)
        self.youtubeLinkLine.setPlaceholderText("https://www.youtube.com/")

    def YoutubeDownloadButonFunction(self):
        self.my_thread = QThread()
        self.worker = Worker(self.youtubeLinkLine.text())
        self.worker.moveToThread(self.my_thread)
        self.worker.programming_signal.connect(self.display)
        self.my_thread.start()
        self.my_thread.started.connect(self.worker.YoutubeDownloadButonThread)
    def display(self,message):
        msg = QMessageBox()
        msg.setWindowTitle("BERKE KARADUMAN")
        msg.setText(message)

        x = msg.exec_()
class Worker(QObject):
    programming_signal = pyqtSignal(str)
    def __init__(self, url):
        super().__init__()
        self.urlLink = url
        self.YoutubeDownloadButonThread()

    def YoutubeDownloadButonThread(self):
        try:
            YouTube(self.urlLink).streams.first().download()
            self.programming_signal.emit("İşlem gerçekleştirildi.")
        except:
            self.programming_signal.emit("İşlem gerçekleştirilemedi.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())