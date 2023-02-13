from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 101)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.youtubeLinkLine = QtWidgets.QLineEdit(self.centralwidget)
        self.youtubeLinkLine.setObjectName("youtubeLinkLine")
        self.gridLayout.addWidget(self.youtubeLinkLine, 0, 1, 1, 1)
        self.youtubeDetailButon = QtWidgets.QPushButton(self.centralwidget)
        self.youtubeDetailButon.setObjectName("youtubeDetailButon")
        self.gridLayout.addWidget(self.youtubeDetailButon, 0, 2, 1, 1)
        self.YoutubeDownloadButon = QtWidgets.QPushButton(self.centralwidget)
        self.YoutubeDownloadButon.setObjectName("YoutubeDownloadButon")
        self.gridLayout.addWidget(self.YoutubeDownloadButon, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Youtube Linkini giriniz:"))
        self.youtubeDetailButon.setText(_translate("MainWindow", "Video Bilgileri"))
        self.YoutubeDownloadButon.setText(_translate("MainWindow", "İndir"))