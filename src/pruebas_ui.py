# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pruebas_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(663, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.activar = QtWidgets.QPushButton(self.centralwidget)
        self.activar.setGeometry(QtCore.QRect(140, 170, 161, 111))
        self.activar.setObjectName("activar")
        self.desactivar = QtWidgets.QPushButton(self.centralwidget)
        self.desactivar.setGeometry(QtCore.QRect(320, 170, 191, 111))
        self.desactivar.setObjectName("desactivar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pruebas"))
        self.activar.setText(_translate("MainWindow", "Activar"))
        self.desactivar.setText(_translate("MainWindow", "Desactivar"))
