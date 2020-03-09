from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys, clipboard, random

cb_state = True
key = 0

def getKey(str):
    str = list(str)
    return int(''.join(str[len(str)-3:len(str)]))

def encry(str, key):
    res = ""
    str = list(str)
    for i in range(0,len(str),1):
        str[i] = ord(str[i])+key
        res += chr(str[i])
    return res

def decry(str, key):
    res = ""
    str =list(str)
    for i in range(0,len(str)-3,1):
        str[i] = ord(str[i])-key
        res += chr(str[i])
    return res

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 425)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.Encrypt.setGeometry(QtCore.QRect(30, 320, 110, 35))
        self.Encrypt.setObjectName("Encrypt")
        self.Decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.Decrypt.setGeometry(QtCore.QRect(180, 320, 110, 35))
        self.Decrypt.setObjectName("Decrypt")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 80, 256, 71))
        self.textBrowser.setReadOnly(False)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 190, 256, 71))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.Label1 = QtWidgets.QLabel(self.centralwidget)
        self.Label1.setGeometry(QtCore.QRect(30, 60, 91, 16))
        self.Label1.setObjectName("Label1")
        self.Label1_2 = QtWidgets.QLabel(self.centralwidget)
        self.Label1_2.setGeometry(QtCore.QRect(30, 170, 91, 16))
        self.Label1_2.setObjectName("Label1_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 276, 120, 20))
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 241, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Encrypt.clicked.connect(self.Encrypt_Func)
        self.Decrypt.clicked.connect(self.Decrypt_Func)

        self.checkBox.stateChanged.connect(self.CheckBox_State)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Encrypt Program"))
        self.Encrypt.setText(_translate("MainWindow", "Encryption"))
        self.Decrypt.setText(_translate("MainWindow", "Decryption"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Label1.setText(_translate("MainWindow", "Data to process"))
        self.Label1_2.setText(_translate("MainWindow", "Result"))
        self.checkBox.setText(_translate("MainWindow", "Copy to clipboard"))
        self.label.setText(_translate("MainWindow", "Encrypt Program"))

    def CheckBox_State(self):
        if self.checkBox.isChecked(): cb_state = True
        else: cb_state = False

    def Encrypt_Func(self):
        key = random.randrange(1,1000)
        txt = self.textBrowser.toPlainText()
        txt = encry(txt, key)
        txt += str(key)
        self.textBrowser_2.clear()
        self.textBrowser_2.append(txt)
        if cb_state: clipboard.copy(txt)

    def Decrypt_Func(self):
        txt = self.textBrowser.toPlainText()
        try:
            key = getKey(txt)
            txt = decry(txt, key)
        except:
            txt = "Error! Please check the string"
        self.textBrowser_2.clear()
        self.textBrowser_2.append(txt)
        if cb_state: clipboard.copy(txt)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
