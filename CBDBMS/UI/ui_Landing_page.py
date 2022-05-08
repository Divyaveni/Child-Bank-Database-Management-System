# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Landing_pageCDwFRe.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *



class Landing_Page(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(661, 519)
        Form.setStyleSheet(u"background-color: rgb(255, 201, 60);\n"
"background-color: rgb(254, 209, 87);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 0, 281, 271))
        self.label.setStyleSheet(u"background-image: url(E:/DBMS PROJRCT/assets/logo3.png);")
        self.label.setPixmap(QPixmap(u"E:/DBMS PROJRCT/assets/logo3.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 280, 211, 41))
        self.label_2.setStyleSheet(u"font: 75 22pt \"Goudy Old Style\";\n"
"color: rgb(21, 84, 93);")
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(True)
        self.label_2.setIndent(27)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 320, 181, 51))
        self.label_3.setStyleSheet(u"font: 75 22pt \"Goudy Old Style\";\n"
"font: 75 26pt \"Goudy Old Style\";\n"
"color: rgb(21, 84, 93);")
        self.label_3.setIndent(16)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 410, 191, 41))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(21, 84, 93);\n"
"selection-background-color: rgb(255, 210, 93);\n"
"selection-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: bold 18pt \"Goudy Old Style\";\n"
"color: rgb(255, 210, 93);\n"
"border-radius: 15px;")
        
        
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(340, 410, 191, 41))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(21, 84, 93);\n"
"selection-background-color: rgb(255, 210, 93);\n"
"selection-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: bold 18pt \"Goudy Old Style\";\n"
"color: rgb(255, 210, 93);\n"
"border-radius: 15px;")
        
        
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(190, 460, 291, 41))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(21, 84, 93);\n"
"font: bold 18pt \"Goudy Old Style\";\n"
"color: rgb(255, 210, 93);\n"
"border-radius: 15px;\n"
"border-color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(255, 210, 93);")
        self.pushButton_3.setCheckable(False)
        

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"BALYA BANK", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Welcome To", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Balya Bank", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Child Login", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Parent Login", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Create an Account", None))
    # retranslateUi

