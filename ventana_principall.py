# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principall.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QWidget, QDesktopWidget, QTableWidgetItem, QTableWidget, QComboBox, QPushButton, QMessageBox
from PROYECTO_FINAL.clases import Estudiante, Materia
from PROYECTO_FINAL.scrapper import semestre_actual
from PROYECTO_FINAL.correos import envia

from typing import List


class Ui_MainWindow_main_prin(object):
    def setupUi_main_prin(self, MainWindow, est:Estudiante):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(393, 649)
        qtRectangle = MainWindow.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        MainWindow.move(qtRectangle.topLeft())
        self.est = est
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbEstd = QtWidgets.QLabel(self.centralwidget)
        self.lbEstd.setGeometry(QtCore.QRect(8, 14, 70, 16))
        self.lbEstd.setObjectName("lbEstd")
        self.pltxtEst = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pltxtEst.setGeometry(QtCore.QRect(77, 10, 290, 25))
        self.pltxtEst.setMaximumSize(QtCore.QSize(16777211, 16777180))
        self.pltxtEst.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pltxtEst.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pltxtEst.setTabStopWidth(70)
        self.pltxtEst.setTabStopDistance(70.0)
        self.pltxtEst.setObjectName("pltxtEst")
        self.pltxtMat = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pltxtMat.setGeometry(QtCore.QRect(77, 80, 111, 25))
        self.pltxtMat.setMaximumSize(QtCore.QSize(16777211, 16777180))
        self.pltxtMat.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pltxtMat.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pltxtMat.setTabStopWidth(70)
        self.pltxtMat.setTabStopDistance(70.0)
        self.pltxtMat.setObjectName("pltxtMat")
        self.lbMat = QtWidgets.QLabel(self.centralwidget)
        self.lbMat.setGeometry(QtCore.QRect(12, 84, 61, 20))
        self.lbMat.setObjectName("lbMat")
        self.lbSeme = QtWidgets.QLabel(self.centralwidget)
        self.lbSeme.setGeometry(QtCore.QRect(200, 86, 61, 16))
        self.lbSeme.setObjectName("lbSeme")
        self.pltxtSeme = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pltxtSeme.setGeometry(QtCore.QRect(259, 80, 106, 25))
        self.pltxtSeme.setMaximumSize(QtCore.QSize(16777211, 16777180))
        self.pltxtSeme.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pltxtSeme.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pltxtSeme.setTabStopWidth(70)
        self.pltxtSeme.setTabStopDistance(70.0)
        self.pltxtSeme.setObjectName("pltxtSeme")
        self.grpMaterias = QtWidgets.QGroupBox(self.centralwidget)
        self.grpMaterias.setGeometry(QtCore.QRect(10, 240, 371, 191))
        self.grpMaterias.setObjectName("grpMaterias")
        self.tableWidget = QtWidgets.QTableWidget(self.grpMaterias)
        self.tableWidget.setGeometry(QtCore.QRect(15, 19, 341, 151))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777208, 16777215))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.estimado = False
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BDiagPattern)
        item.setForeground(brush)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 2, item)
        self.pltxtCarre = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pltxtCarre.setGeometry(QtCore.QRect(77, 46, 290, 25))
        self.pltxtCarre.setMaximumSize(QtCore.QSize(16777211, 16777180))
        self.pltxtCarre.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pltxtCarre.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pltxtCarre.setTabStopWidth(70)
        self.pltxtCarre.setTabStopDistance(70.0)
        self.pltxtCarre.setObjectName("pltxtCarre")
        self.lbCarr = QtWidgets.QLabel(self.centralwidget)
        self.lbCarr.setGeometry(QtCore.QRect(21, 50, 61, 16))
        self.lbCarr.setObjectName("lbCarr")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 130, 371, 101))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 101, 16))
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(110, 26, 70, 25))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(290, 27, 70, 25))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(190, 30, 101, 16))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(110, 65, 70, 25))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 81, 16))
        self.label_3.setObjectName("label_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(290, 65, 70, 25))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(202, 70, 91, 16))
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 440, 371, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 101, 16))
        self.label_5.setObjectName("label_5")
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(110, 26, 70, 25))
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_6.setGeometry(QtCore.QRect(290, 27, 70, 25))
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(190, 30, 101, 16))
        self.label_6.setObjectName("label_6")
        self.plainTextEdit_7 = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_7.setGeometry(QtCore.QRect(110, 65, 70, 25))
        self.plainTextEdit_7.setObjectName("plainTextEdit_7")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(30, 70, 81, 16))
        self.label_7.setObjectName("label_7")
        self.plainTextEdit_8 = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_8.setGeometry(QtCore.QRect(290, 65, 70, 25))
        self.plainTextEdit_8.setObjectName("plainTextEdit_8")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(198, 70, 91, 16))
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 562, 75, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 393, 21))
        self.menubar.setObjectName("menubar")
        self.menuARCHIVO = QtWidgets.QMenu(self.menubar)
        self.menuARCHIVO.setObjectName("menuARCHIVO")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuARCHIVO.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.tomar_datos)
        self.menuARCHIVO.triggered.connect(self.enviar_est)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Estimador de indice"))
        self.lbEstd.setText(_translate("MainWindow", "ESTUDIANTE:"))
        self.lbMat.setText(_translate("MainWindow", "MATRICULA:"))
        self.lbSeme.setText(_translate("MainWindow", "SEMESTRE:"))
        self.grpMaterias.setTitle(_translate("MainWindow", "MATERIAS ACTUALES"))
        self.columnas = ["Materia", "Cred", "Calf"]
        self.tableWidget.setHorizontalHeaderLabels(self.columnas)
        self.tableWidget.setColumnWidth(0,150)
        self.tableWidget.setColumnWidth(1, 65)
        self.tableWidget.setColumnWidth(2, 65)
        self.tableWidget.setSortingEnabled(False)
        #item = self.tableWidget.item(0, 0)
        #item.setText(_translate("MainWindow", "Ingenieria Economica"))
        #item = self.tableWidget.item(0, 1)
        #item.setText(_translate("MainWindow", "3"))
        #item = self.tableWidget.item(0, 2)
        #item.setText(_translate("MainWindow", "A"))

        self.lbCarr.setText(_translate("MainWindow", "CARRERA:"))
        self.groupBox.setTitle(_translate("MainWindow", "Información Academica Actual"))
        self.label.setText(_translate("MainWindow", "Creditos acumulados"))
        self.label_2.setText(_translate("MainWindow", "Puntos acumulados"))
        self.label_3.setText(_translate("MainWindow", "Cant. Materias"))
        self.label_4.setText(_translate("MainWindow", "Indice Acumulado"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Información Academica Estimado"))
        self.label_5.setText(_translate("MainWindow", "Creditos acumulados"))
        self.label_6.setText(_translate("MainWindow", "Puntos acumulados"))
        self.label_7.setText(_translate("MainWindow", "Indice Semestral"))
        self.label_8.setText(_translate("MainWindow", "Indice Acumulado"))
        self.pushButton.setText(_translate("MainWindow", "ESTIMAR"))
        self.menuARCHIVO.setTitle(_translate("MainWindow", "Enviar Estimacion"))
        self.pltxtEst.setPlainText(_translate("MainWindow", str(self.est.nombre)))
        self.pltxtCarre.setPlainText(_translate("MainWindow", str(self.est.carrera)))
        self.pltxtMat.setPlainText(_translate("MainWindow", str(self.est.id)))
        self.pltxtSeme.setPlainText(_translate("MainWindow", str(semestre_actual())))
        self.plainTextEdit.setPlainText(_translate("MainWindow", str(self.est.creditos_acu)))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", str(self.est.puntos_acumu)))
        self.plainTextEdit_3.setPlainText(_translate("MainWindow", str(self.est.cant_materias_curso)))
        self.plainTextEdit_4.setPlainText(_translate("MainWindow", str(self.est.indice_acu)))
        tableWidget = QTableWidget()
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        tableWidget.insertRow(currentRowCount)
        letras = [" ", "A", "B", "C", "D", "F", "R"]
        for mat in self.est.materias:
            rowPosition = self.tableWidget.rowCount() - 1
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(mat.nombre))
            self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(mat.creditos))
            combo = QComboBox()
            combo.setObjectName(f"combo{rowPosition}")
            for t in letras:
                combo.addItem(t)
            self.tableWidget.setCellWidget(rowPosition,2,combo)

    def tomar_datos(self):
        self.estimado = True
        i = 0
        valor : QComboBox
        for r in range(self.tableWidget.rowCount()):
            for c in range(self.tableWidget.columnCount()):
                widget = self.tableWidget.cellWidget(r, c)
                if isinstance(widget, QComboBox):
                    current_value = widget.currentText()
                    self.est.materias[r].calificacion = current_value
        materias: List[Materia] = []
        for m in self.est.materias:
            materias.append(m)

        self.materias_est = materias
        PUNTOS_LETRAS = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
        puntos = 0
        for m in materias:
            puntos += (PUNTOS_LETRAS.get(m.calificacion) * float(m.creditos))
        #print(puntos)
        credi = float(self.est.creditos_cursando)
        indice_semestral = float(puntos) / float(credi)
        self.indice_semestral = indice_semestral
        #print(round(indice_semestral,1))
        puntos_ac = float(self.est.puntos_acumu)
        puntos_est = puntos_ac + puntos
        self.puntos_acu_estimados =puntos_est
        #print(puntos_est)
        credi_acu = float (self.est.creditos_acu)
        credi_est = credi + credi_acu
        self.creditos_acu_est = credi_est
        #print(credi_est)
        indice_acu_est = puntos_est/credi_est
        self.indice_acumulado_est = indice_acu_est
        #print(round(indice_acu_est,1))

        self.plainTextEdit_5.setPlainText(str(round(credi_est,1)))
        self.plainTextEdit_6.setPlainText(str(round(puntos_est,1)))
        self.plainTextEdit_7.setPlainText(str(round(indice_semestral, 1)))
        self.plainTextEdit_8.setPlainText(str(round(indice_acu_est, 1)))


    def enviar_est(self):
        if self.estimado:
            try:
                envia(self.est, self.materias_est,self.indice_semestral,self.puntos_acu_estimados,self.creditos_acu_est,self.indice_acumulado_est)
            except:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Error al enviar CORREO')











