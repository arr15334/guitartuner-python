# -*- coding: utf-8 -*-
import time
from PyQt4 import QtCore, QtGui
import sys
from afinador import afinador
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1206, 1066)
        MainWindow.setAcceptDrops(True)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(76, 76, 76);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridFrame = QtGui.QFrame(self.centralwidget)
        self.gridFrame.setGeometry(QtCore.QRect(80, 100, 961, 391))
        self.gridFrame.setStyleSheet(_fromUtf8("background-color: rgb(214, 214, 214);\n"
"background-image: url(:/newPrefix/D:/UVG/g70.png);"))
        self.gridFrame.setObjectName(_fromUtf8("gridFrame"))
        self.gridLayout = QtGui.QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(310, 10, 461, 81))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet(_fromUtf8("color: rgb(170, 170, 127);\n"
"font: 28pt \"AcmeFont\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 577, 131, 41))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 640, 131, 41))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 580, 131, 41))
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 640, 131, 41))
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(410, 640, 131, 41))
        self.pushButton_5.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(410, 580, 131, 41))
        self.pushButton_6.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 500, 861, 71))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(85, 255, 127);\n"
"color: rgb(85, 170, 255);\n"
"font: 18pt \"AcmeFont\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalSlider = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(590, 600, 521, 61))
        self.horizontalSlider.setAcceptDrops(True)
        self.horizontalSlider.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.horizontalSlider.setMinimum(50)
        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setProperty("value", 500)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(580, 680, 541, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(490, 720, 311, 71))
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(85, 170, 255);\n"
"font: 12pt \"AcmeFont\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lcdNumber_2 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(810, 710, 201, 91))
        self.lcdNumber_2.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(490, 820, 311, 81))
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(85, 170, 255);\n"
"font: 12pt \"AcmeFont\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lcdNumber_3 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(810, 810, 201, 91))
        self.lcdNumber_3.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.lcdNumber_3.setObjectName(_fromUtf8("lcdNumber_3"))
        self.verticalFrame_2 = QtGui.QFrame(self.centralwidget)
        self.verticalFrame_2.setGeometry(QtCore.QRect(570, 590, 571, 81))
        self.verticalFrame_2.setStyleSheet(_fromUtf8("background-color: rgba(0,0,0,0.3)"))
        self.verticalFrame_2.setObjectName(_fromUtf8("verticalFrame_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 930, 311, 71))
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(85, 170, 255);\n"
"font: 12pt \"AcmeFont\";"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1206, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Guitar - Tuner", None))
        self.pushButton.setText(_translate("MainWindow", "1", None))
        self.pushButton.clicked.connect(self.handleButton1)
        self.pushButton_2.setText(_translate("MainWindow", "2", None))
        self.pushButton_2.clicked.connect(self.handleButton2)
        self.pushButton_3.setText(_translate("MainWindow", "3", None))
        self.pushButton_3.clicked.connect(self.handleButton3)
        self.pushButton_4.setText(_translate("MainWindow", "4", None))
        self.pushButton_4.clicked.connect(self.handleButton4)
        self.pushButton_5.setText(_translate("MainWindow", "5", None))
        self.pushButton_5.clicked.connect(self.handleButton5)
        self.pushButton_6.setText(_translate("MainWindow", "6", None))
        self.pushButton_6.clicked.connect(self.handleButton6)
        self.label_2.setText(_translate("MainWindow", "Seleccione el numero de la cuerda a afinar: ", None))
        self.label_3.setText(_translate("MainWindow", "50                 200                                  500                      700                                  1000", None))
        self.label_4.setText(_translate("MainWindow", "Frecuencia actual de la cuerda:", None))
        self.label_5.setText(_translate("MainWindow", "Frecuencia para estar afinada:", None))
        self.label_6.setText(_translate("MainWindow", "", None))


    def handleButton1(self):
        self.label_6.setText(_translate("MainWindow", "Recording...", None))
        time.sleep(3)
        """
        QtGui.QMessageBox.information(self,
                                      'Message',
                                      "En este instante el sonido sera grabado y procesado")
        """
        a,b,c,d = afinador(1)
        time.sleep(3)
        self.horizontalSlider.setProperty("value", int(a))
        self.lcdNumber_2.display(int(b))
        self.lcdNumber_3.display(int(c))
        #self.label_6.setText(_translate("MainWindow", str(d), None))
        QtGui.QMessageBox.information(self,
                                      'Message',
                                      str(d))
    def handleButton2(self):
        a, b, c, d = afinador(2)
        self.horizontalSlid
        self.horizontalSlider.setProperty("value", int(a))
        self.lcdNumber_2.display(int(b))
        self.lcdNumber_3.display(int(c))
        QtGui.QMessageBox.information(self,
                                      'Message',
                                      str(d))
    def handleButton3(self):
        a, b, c, d = afinador(3)
        self.horizontalSlider.setProperty("value", int(a))
        self.lcdNumber_2.display(int(b))
        self.lcdNumber_3.display(int(c))
        QtGui.QMessageBox.information(self,
                                      'Message',
                                      str(d))
    def handleButton4(self):
        a, b, c, d = afinador(4)
        self.horizontalSlider.setProperty("value", int(a))
        self.lcdNumber_2.display(int(b))
        self.lcdNumber_3.display(int(c))
        QtGui.QMessageBox.information(self,
                                      'Message',
                                      str(d))
    def handleButton5(self):
        a, b, c, d = afinador(5)
        self.horizontalSlider.setProperty("value", int(a))
        self.lcdNumber_2.display(int(b))
        self.lcdNumber_3.display(int(c))
        QtGui.QMessageBox.information(self,
                                      'Message',
                                      str(d))
    def handleButton6(self):
        a, b, c, d = afinador(6)
        self.horizontalSlider.setProperty("value", int(a))
        self.lcdNumber_2.display(int(b))
        self.lcdNumber_3.display(int(c))
        QtGui.QMessageBox.information(self,
                                      'Message',
                                      str(d))

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainwin = MyForm()
    mainwin.show()
    sys.exit(app.exec_())
