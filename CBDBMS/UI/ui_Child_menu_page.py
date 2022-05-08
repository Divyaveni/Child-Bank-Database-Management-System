# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Child_menu_pageJojgRR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(754, 465)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 210, 93);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-220, 0, 441, 471))
        self.line.setStyleSheet(u"background-color: rgb(21, 82, 93);\n"
"background-color: rgb(21, 84, 93);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 0, 111, 121))
        self.label.setStyleSheet(u"\n"
"background-image: url(assets/logo3_1.png);")
        self.label.setPixmap(QPixmap(u"assets/logo3_1.png"))
        self.label.setScaledContents(True)
        self.transaction_btn = QPushButton(self.centralwidget)
        self.transaction_btn.setObjectName(u"transaction_btn")
        self.transaction_btn.setGeometry(QRect(10, 200, 201, 41))
        self.transaction_btn.setStyleSheet(u"QPushButton {\n"
"font: italic 18pt \"Goudy Old Style\";\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(14, 54, 61);\n"
"color:rgb(255,212,93);\n"
"}")
        self.transfer_btn = QPushButton(self.centralwidget)
        self.transfer_btn.setObjectName(u"transfer_btn")
        self.transfer_btn.setGeometry(QRect(10, 260, 201, 41))
        self.transfer_btn.setStyleSheet(u"QPushButton {\n"
"font: italic 18pt \"Goudy Old Style\";\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(14, 54, 61);\n"
"color:rgb(255,212,93);\n"
"}")
        self.deposit_btn = QPushButton(self.centralwidget)
        self.deposit_btn.setObjectName(u"deposit_btn")
        self.deposit_btn.setGeometry(QRect(10, 320, 201, 41))
        self.deposit_btn.setStyleSheet(u"QPushButton {\n"
"font: italic 18pt \"Goudy Old Style\";\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(14, 54, 61);\n"
"color:rgb(255,212,93);\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 100, 221, 41))
        self.label_2.setStyleSheet(u"background-color: rgb(21, 84, 93);\n"
"color: rgb(255, 210, 93);\n"
"font: 75 24pt \"Goudy Old Style\";")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(230, 110, 521, 351))
        self.transaction_page = QWidget()
        self.transaction_page.setObjectName(u"transaction_page")
        self.label_10 = QLabel(self.transaction_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(140, 10, 221, 41))
        self.label_10.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 20pt \"Goudy Old Style\";")
        self.History_table = QTableWidget(self.transaction_page)
        self.History_table.setObjectName(u"History_table")
        self.History_table.setGeometry(QRect(10, 61, 491, 251))
        self.History_table.setStyleSheet(u"font: 75 14pt \"Goudy Old Style\";\n"
"color: rgb(0, 0, 0);")
        self.stackedWidget.addWidget(self.transaction_page)
        self.withdraw_page = QWidget()
        self.withdraw_page.setObjectName(u"withdraw_page")
        self.stackedWidget.addWidget(self.withdraw_page)
        self.depost_page = QWidget()
        self.depost_page.setObjectName(u"depost_page")
        self.label_5 = QLabel(self.depost_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 30, 111, 41))
        self.label_5.setStyleSheet(u"background-color: rgb(255, 210, 93);\n"
"color: rgb(21, 84, 93);\n"
"font: 75 24pt \"Goudy Old Style\";\n"
" ")
        self.label_18 = QLabel(self.depost_page)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 130, 251, 41))
        self.label_18.setStyleSheet(u"background-color: rgb(255, 210, 93);\n"
"color: rgb(21, 84, 93);\n"
"font: 75 18pt \"Goudy Old Style\";\n"
" ")
        self.Deposit_amnt_edt = QLineEdit(self.depost_page)
        self.Deposit_amnt_edt.setObjectName(u"Deposit_amnt_edt")
        self.Deposit_amnt_edt.setGeometry(QRect(310, 140, 141, 21))
        self.deposit_btn_child = QPushButton(self.depost_page)
        self.deposit_btn_child.setObjectName(u"deposit_btn_child")
        self.deposit_btn_child.setGeometry(QRect(140, 210, 201, 41))
        self.deposit_btn_child.setStyleSheet(u"QPushButton {\n"
"font: italic 18pt \"Goudy Old Style\";\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(14, 54, 61);\n"
"color:rgb(255,212,93);\n"
"}")
        self.stackedWidget.addWidget(self.depost_page)
        self.transfer_page = QWidget()
        self.transfer_page.setObjectName(u"transfer_page")
        self.Transfer_widget = QStackedWidget(self.transfer_page)
        self.Transfer_widget.setObjectName(u"Transfer_widget")
        self.Transfer_widget.setGeometry(QRect(20, 69, 481, 251))
        self.verify_account_page = QWidget()
        self.verify_account_page.setObjectName(u"verify_account_page")
        self.label_6 = QLabel(self.verify_account_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 50, 211, 41))
        self.label_6.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.acc_edt = QLineEdit(self.verify_account_page)
        self.acc_edt.setObjectName(u"acc_edt")
        self.acc_edt.setGeometry(QRect(260, 60, 181, 31))
        self.acc_edt.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 18pt \"Goudy Old Style\";")
        self.verify_btn = QPushButton(self.verify_account_page)
        self.verify_btn.setObjectName(u"verify_btn")
        self.verify_btn.setGeometry(QRect(130, 140, 201, 41))
        self.verify_btn.setStyleSheet(u"QPushButton {\n"
"font: italic 18pt \"Goudy Old Style\";\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(14, 54, 61);\n"
"color:rgb(255,212,93);\n"
"}")
        self.Transfer_widget.addWidget(self.verify_account_page)
        self.amount_enter_page = QWidget()
        self.amount_enter_page.setObjectName(u"amount_enter_page")
        self.label_13 = QLabel(self.amount_enter_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(90, 40, 81, 21))
        self.label_13.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.Name_edt = QLineEdit(self.amount_enter_page)
        self.Name_edt.setObjectName(u"Name_edt")
        self.Name_edt.setGeometry(QRect(240, 30, 161, 31))
        self.Name_edt.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 16pt \"Goudy Old Style\";")
        self.label_14 = QLabel(self.amount_enter_page)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(90, 80, 121, 21))
        self.label_14.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.Name_edt_2 = QLineEdit(self.amount_enter_page)
        self.Name_edt_2.setObjectName(u"Name_edt_2")
        self.Name_edt_2.setGeometry(QRect(240, 70, 161, 31))
        self.Name_edt_2.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 16pt \"Goudy Old Style\";")
        self.Name_edt_3 = QLineEdit(self.amount_enter_page)
        self.Name_edt_3.setObjectName(u"Name_edt_3")
        self.Name_edt_3.setGeometry(QRect(240, 110, 161, 31))
        self.Name_edt_3.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 16pt \"Goudy Old Style\";")
        self.label_15 = QLabel(self.amount_enter_page)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(90, 120, 141, 21))
        self.label_15.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.confirm_btn = QPushButton(self.amount_enter_page)
        self.confirm_btn.setObjectName(u"confirm_btn")
        self.confirm_btn.setGeometry(QRect(150, 190, 201, 41))
        self.confirm_btn.setStyleSheet(u"QPushButton {\n"
"font: italic 18pt \"Goudy Old Style\";\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(14, 54, 61);\n"
"color:rgb(255,212,93);\n"
"}")
        self.label_19 = QLabel(self.amount_enter_page)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(90, 160, 141, 21))
        self.label_19.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.message_edt = QLineEdit(self.amount_enter_page)
        self.message_edt.setObjectName(u"message_edt")
        self.message_edt.setGeometry(QRect(240, 150, 161, 31))
        self.message_edt.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 16pt \"Goudy Old Style\";")
        self.Transfer_widget.addWidget(self.amount_enter_page)
        self.Confirm_amount_page = QWidget()
        self.Confirm_amount_page.setObjectName(u"Confirm_amount_page")
        self.label_12 = QLabel(self.Confirm_amount_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(80, 60, 131, 21))
        self.label_12.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.lineEdit = QLineEdit(self.Confirm_amount_page)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(280, 60, 161, 31))
        self.lineEdit.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 18pt \"Goudy Old Style\";")
        self.label_16 = QLabel(self.Confirm_amount_page)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(80, 100, 131, 21))
        self.label_16.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.lineEdit_2 = QLineEdit(self.Confirm_amount_page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(280, 100, 161, 31))
        self.lineEdit_2.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 18pt \"Goudy Old Style\";")
        self.Transfer_btn = QPushButton(self.Confirm_amount_page)
        self.Transfer_btn.setObjectName(u"Transfer_btn")
        self.Transfer_btn.setGeometry(QRect(130, 160, 201, 41))
        self.Transfer_btn.setStyleSheet(u"QPushButton {\n"
"font: italic 18pt \"Goudy Old Style\";\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(14, 54, 61);\n"
"color:rgb(255,212,93);\n"
"}")
        self.Transfer_widget.addWidget(self.Confirm_amount_page)
        self.label_11 = QLabel(self.transfer_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(190, 20, 151, 41))
        self.label_11.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 20pt \"Goudy Old Style\";")
        self.stackedWidget.addWidget(self.transfer_page)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(230, 10, 201, 41))
        self.label_7.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 20pt \"Goudy Old Style\";")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(480, 10, 151, 41))
        self.label_8.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 20pt \"Goudy Old Style\";")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(230, 50, 231, 41))
        self.label_9.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 20pt \"Goudy Old Style\";")
        self.Used_lbl = QLabel(self.centralwidget)
        self.Used_lbl.setObjectName(u"Used_lbl")
        self.Used_lbl.setGeometry(QRect(480, 50, 161, 41))
        self.Used_lbl.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 20pt \"Goudy Old Style\";")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(50, 150, 121, 21))
        self.label_17.setStyleSheet(u"background-color: rgb(21, 84, 93);\n"
"color: rgb(255, 210, 93);\n"
"font: 75 18pt \"Goudy Old Style\";")
        self.logout_btn = QPushButton(self.centralwidget)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setGeometry(QRect(660, 20, 81, 41))
        self.logout_btn.setStyleSheet(u"QPushButton {\n"
"font: italic 18pt \"Goudy Old Style\";\n"
"background-color:rgb(14, 54, 61);\n"
"color:rgb(255,212,93);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.Transfer_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.transaction_btn.setText(QCoreApplication.translate("MainWindow", u"Transaction History", None))
        self.transfer_btn.setText(QCoreApplication.translate("MainWindow", u"Transfer", None))
        self.deposit_btn.setText(QCoreApplication.translate("MainWindow", u"Request Funds", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pavan Kumar", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Transaction History", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Deposit", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Enter Amount to Request", None))
        self.deposit_btn_child.setText(QCoreApplication.translate("MainWindow", u"Request", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Enter Account Number", None))
        self.verify_btn.setText(QCoreApplication.translate("MainWindow", u"Verify", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Enter Amount", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Re- Enter Amount", None))
        self.confirm_btn.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.Transfer_btn.setText(QCoreApplication.translate("MainWindow", u"Transfer", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TRANSFER", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Available Balance :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Rs. 20000", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Amount used today :", None))
        self.Used_lbl.setText(QCoreApplication.translate("MainWindow", u"Rs. 1000", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"2360588915", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    # retranslateUi

