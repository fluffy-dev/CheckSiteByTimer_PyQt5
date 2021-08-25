# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(372, 497)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.repetition = QtWidgets.QLabel(self.centralwidget)
        self.repetition.setObjectName("repetition")
        self.gridLayout.addWidget(self.repetition, 7, 0, 1, 1)
        self.timerLine = QtWidgets.QLineEdit(self.centralwidget)
        self.timerLine.setObjectName("timerLine")
        self.gridLayout.addWidget(self.timerLine, 3, 0, 1, 1)
        self.url = QtWidgets.QLabel(self.centralwidget)
        self.url.setObjectName("url")
        self.gridLayout.addWidget(self.url, 4, 0, 1, 1)
        self.repetitionSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.repetitionSpinBox.setObjectName("repetitionSpinBox")
        self.gridLayout.addWidget(self.repetitionSpinBox, 8, 0, 1, 1)
        self.urlLine = QtWidgets.QLineEdit(self.centralwidget)
        self.urlLine.setObjectName("urlLine")
        self.gridLayout.addWidget(self.urlLine, 6, 0, 1, 1)
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setObjectName("start")
        self.gridLayout.addWidget(self.start, 9, 0, 1, 1)
        self.timer = QtWidgets.QLabel(self.centralwidget)
        self.timer.setObjectName("timer")
        self.gridLayout.addWidget(self.timer, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 2, 1, 1)
        self.output = QtWidgets.QListWidget(self.centralwidget)
        self.output.setObjectName("output")
        self.gridLayout_2.addWidget(self.output, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.repetition.setText(_translate("MainWindow", "repetition(qty):"))
        self.url.setText(_translate("MainWindow", "url(website):"))
        self.start.setText(_translate("MainWindow", "start"))
        self.timer.setText(_translate("MainWindow", "timer(seconds):"))