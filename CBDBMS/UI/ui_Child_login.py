# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Child_loginZrKFdI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *



class Child_login(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(595, 528)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color: rgb(255, 210, 93);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 0, 201, 191))
        self.label.setStyleSheet(u"background-image: url(assets/logo3.JPG);")
        self.label.setPixmap(QPixmap(u"assets/logo3.JPG"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 190, 171, 61))
        self.label_2.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 22pt \"Goudy Old Style\";")
        self.label_2.setIndent(8)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 280, 111, 41))
        font = QFont()
        font.setFamily(u"Goudy Old Style")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(21, 84, 93);")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 320, 111, 41))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(21, 84, 93);")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(300, 280, 151, 31))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Goudy Old Style\";")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(300, 330, 151, 31))
        self.lineEdit_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Goudy Old Style\";")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 410, 191, 51))
        self.pushButton.setStyleSheet(u"background-color: rgb(21, 84, 93);\n"
"color: rgb(255, 210, 93);\n"
"font: bold 24pt \"Goudy Old Style\";\n"
"border-radius:15px;\n"
"border-color: rgb(255, 255, 255);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Child Login", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Password", None))
        self.lineEdit_2.setInputMask("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"Login", None))
    # retranslateUi

