# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Parent_LoginbrRFPI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Parent_Login(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(779, 477)
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-800, 0, 1581, 481))
        self.line.setStyleSheet(u"background-color: rgb(21, 82, 93);\n"
"background-color: rgb(21, 84, 93);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 0, 191, 201))
        self.label.setStyleSheet(u"background-image: url(assets/logo3_1.png);")
        self.label.setPixmap(QPixmap(u"assets/logo3_1.png"))
        self.label.setScaledContents(True)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 200, 111, 51))
        self.label_3.setStyleSheet(u"color: rgb(255, 210, 93);\n"
"font: 75 18pt \"Goudy Old Style\";")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(210, 260, 111, 51))
        self.label_4.setStyleSheet(u"color: rgb(255, 210, 93);\n"
"font: 75 18pt \"Goudy Old Style\";")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(440, 210, 151, 31))
        self.lineEdit.setStyleSheet(u"font: 75 14pt \"Goudy Old Style\";")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(440, 270, 151, 31))
        self.lineEdit_2.setStyleSheet(u"font: 75 14pt \"Goudy Old Style\";")
        self.Login_btn = QPushButton(Form)
        self.Login_btn.setObjectName(u"Login_btn")
        self.Login_btn.setGeometry(QRect(310, 360, 191, 41))
        self.Login_btn.setStyleSheet(u"font: italic 18pt \"Goudy Old Style\";\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"border-radius: 15px;")
        self.Login_btn_2 = QPushButton(Form)
        self.Login_btn_2.setObjectName(u"Login_btn_2")
        self.Login_btn_2.setGeometry(QRect(20, 10, 91, 41))
        self.Login_btn_2.setStyleSheet(u"font: italic 18pt \"Goudy Old Style\";\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"border-radius: 15px;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Password", None))
        self.Login_btn.setText(QCoreApplication.translate("Form", u"Login", None))
        self.Login_btn_2.setText(QCoreApplication.translate("Form", u"Back", None))
    # retranslateUi

