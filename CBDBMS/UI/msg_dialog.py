# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialogue_boxsOtayd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 248)
        Dialog.setStyleSheet(u"background-color: rgb(21, 84, 93);")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(160, 200, 81, 32))
        self.buttonBox.setStyleSheet(u"color: rgb(255, 210, 93);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.message_lbl = QLabel(Dialog)
        self.message_lbl.setObjectName(u"message_lbl")
        self.message_lbl.setGeometry(QRect(0, 140, 401, 41))
        self.message_lbl.setStyleSheet(u"color: rgb(255, 210, 93);\n"
"font: 75 18pt \"Goudy Old Style\";")
        self.message_lbl.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 10, 121, 111))
        self.label_2.setStyleSheet(u"background-image: url(assets/logo3_1.png);")
        self.label_2.setPixmap(QPixmap(u"assets/logo3_1.png"))
        self.label_2.setScaledContents(True)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.message_lbl.setText(QCoreApplication.translate("Dialog", u"Transaction Successfull", None))
        self.label_2.setText("")
    # retranslateUi

