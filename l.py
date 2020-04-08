# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
from PROYECTO_FINAL.clases import Estudiante, Materia
from PROYECTO_FINAL.scrapper import *
from PROYECTO_FINAL.ventana_principall import Ui_MainWindow_main_prin

class Ui_MainWindow_login(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(362, 376)
        self.cerrar = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lemat = QtWidgets.QLineEdit(self.centralwidget)
        self.lemat.setGeometry(QtCore.QRect(80, 150, 250, 25))
        self.lemat.setObjectName("lemat")
        self.lecon = QtWidgets.QLineEdit(self.centralwidget)
        self.lecon.setGeometry(QtCore.QRect(80, 186, 250, 25))
        self.lecon.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lecon.setObjectName("lecon")
        self.btnent = QtWidgets.QPushButton(self.centralwidget)
        self.btnent.setGeometry(QtCore.QRect(150, 240, 75, 41))
        self.btnent.setObjectName("btnent")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(40, 310, 291, 23))
        self.progressBar.hide()
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lbmat = QtWidgets.QLabel(self.centralwidget)
        self.lbmat.setGeometry(QtCore.QRect(30, 156, 47, 13))
        self.lbmat.setObjectName("lbmat")
        self.lbcon = QtWidgets.QLabel(self.centralwidget)
        self.lbcon.setGeometry(QtCore.QRect(10, 190, 61, 16))
        self.lbcon.setObjectName("lbcon")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 290, 111, 16))
        self.label.setObjectName("label")
        self.label.hide()
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 10, 125, 125))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("usuario.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 362, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.estudiante: Estudiante
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.progressBar.setProperty("value", 100)
        self.btnent.clicked.connect(self.abrir)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Estimador de indice"))
        self.btnent.setText(_translate("MainWindow", "Entrar"))
        self.lbmat.setText(_translate("MainWindow", "Matricula"))
        self.lbcon.setText(_translate("MainWindow", "Constraseña"))
        self.label.setText(_translate("MainWindow", "Recolectando datos"))

    def abrir(self):
        estudiante = self.recolectar_datos()
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_main_prin()
        self.ui.setupUi_main_prin(self.ventana, estudiante)
        self.ventana.show()
        self.cerrar.destroy()

    def recolectar_datos(self):
        if ((self.lemat.text() == "") or (self.lecon.text() == "")):
            print("error")
        else:
            user = self.lemat.text()
            password = self.lecon.text()
            self.label.show()
            self.progressBar.show()
            self.progressBar.setProperty("value", 25)
            estudiante = get_estudiante(user, password)
            self.progressBar.setProperty("value", 50)
            time.sleep(5)
            self.progressBar.setProperty("value", 100)
            self.estudiante = estudiante
        return estudiante


