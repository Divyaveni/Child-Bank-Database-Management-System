# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Parent_displayqrWkZZ.ui'
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
        MainWindow.resize(751, 466)
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
        self.label.setGeometry(QRect(60, 10, 111, 121))
        self.label.setStyleSheet(u"\n"
"background-image: url(assets/logo3_1.png);")
        self.label.setPixmap(QPixmap(u"assets/logo3_1.png"))
        self.label.setScaledContents(True)
        self.Approval_btn = QPushButton(self.centralwidget)
        self.Approval_btn.setObjectName(u"Approval_btn")
        self.Approval_btn.setGeometry(QRect(10, 240, 201, 41))
        self.Approval_btn.setStyleSheet(u"QPushButton {\n"
"font: italic 18pt \"Goudy Old Style\";\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"border-style : inset;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(14, 54, 61);\n"
"color:rgb(255,212,93);\n"
"}\n"
"")
        self.transfer_btn = QPushButton(self.centralwidget)
        self.transfer_btn.setObjectName(u"transfer_btn")
        self.transfer_btn.setGeometry(QRect(10, 290, 201, 41))
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
        self.transaction_btn = QPushButton(self.centralwidget)
        self.transaction_btn.setObjectName(u"transaction_btn")
        self.transaction_btn.setGeometry(QRect(10, 340, 201, 41))
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
        self.transaction_lmt_btn = QPushButton(self.centralwidget)
        self.transaction_lmt_btn.setObjectName(u"transaction_lmt_btn")
        self.transaction_lmt_btn.setGeometry(QRect(10, 390, 201, 41))
        self.transaction_lmt_btn.setStyleSheet(u"QPushButton {\n"
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
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(250, 10, 231, 41))
        self.label_7.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 16pt \"Goudy Old Style\";")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 140, 181, 41))
        self.label_8.setStyleSheet(u"color: rgb(255, 212, 93);\n"
"background-color: rgb(21, 84, 93);\n"
"font: 75 16pt \"Goudy Old Style\";")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(490, 10, 151, 41))
        self.label_9.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 16pt \"Goudy Old Style\";")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(229, 100, 521, 361))
        self.Approval_message_page = QWidget()
        self.Approval_message_page.setObjectName(u"Approval_message_page")
        self.RequestsWidget = QStackedWidget(self.Approval_message_page)
        self.RequestsWidget.setObjectName(u"RequestsWidget")
        self.RequestsWidget.setGeometry(QRect(10, 100, 501, 241))
        self.Transfer_request_page = QWidget()
        self.Transfer_request_page.setObjectName(u"Transfer_request_page")
        self.transfer_request_table = QTableWidget(self.Transfer_request_page)
        self.transfer_request_table.setObjectName(u"transfer_request_table")
        self.transfer_request_table.setGeometry(QRect(15, 20, 471, 171))
        self.transfer_request_table.setStyleSheet(u"font: 75 14pt \"Goudy Old Style\";\n"
"color: rgb(0, 0, 0);")
        self.approve_transaction_btn = QPushButton(self.Transfer_request_page)
        self.approve_transaction_btn.setObjectName(u"approve_transaction_btn")
        self.approve_transaction_btn.setGeometry(QRect(60, 200, 131, 31))
        self.approve_transaction_btn.setStyleSheet(u"QPushButton {\n"
"font: italic 14pt \"Goudy Old Style\";\n"
"background-color:rgb(14, 54, 61);\n"
"color:rgb(255,212,93);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"border-style : inset;\n"
"}\n"
"QPushButton:hover {\n"
"\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"}\n"
"")
        self.deny_transaction_btn = QPushButton(self.Transfer_request_page)
        self.deny_transaction_btn.setObjectName(u"deny_transaction_btn")
        self.deny_transaction_btn.setGeometry(QRect(320, 200, 131, 31))
        self.deny_transaction_btn.setStyleSheet(u"QPushButton {\n"
"font: italic 14pt \"Goudy Old Style\";\n"
"background-color:rgb(14, 54, 61);\n"
"color:rgb(255,212,93);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"border-style : inset;\n"
"}\n"
"QPushButton:hover {\n"
"\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"}\n"
"")
        self.RequestsWidget.addWidget(self.Transfer_request_page)
        self.Deposit_request_page = QWidget()
        self.Deposit_request_page.setObjectName(u"Deposit_request_page")
        self.deposit_requests_table = QTableWidget(self.Deposit_request_page)
        self.deposit_requests_table.setObjectName(u"deposit_requests_table")
        self.deposit_requests_table.setGeometry(QRect(20, 20, 471, 171))
        self.deposit_requests_table.setStyleSheet(u"font: 75 12pt \"Goudy Old Style\";\n"
"color: rgb(0, 0, 0);")
        self.approve_deposit_btn = QPushButton(self.Deposit_request_page)
        self.approve_deposit_btn.setObjectName(u"approve_deposit_btn")
        self.approve_deposit_btn.setGeometry(QRect(90, 200, 131, 31))
        self.approve_deposit_btn.setStyleSheet(u"QPushButton {\n"
"font: italic 14pt \"Goudy Old Style\";\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"border-style : inset;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(14, 54, 61);\n"
"color:rgb(255,212,93);\n"
"}\n"
"")
        self.deny_deposit_btn = QPushButton(self.Deposit_request_page)
        self.deny_deposit_btn.setObjectName(u"deny_deposit_btn")
        self.deny_deposit_btn.setGeometry(QRect(300, 200, 131, 31))
        self.deny_deposit_btn.setStyleSheet(u"QPushButton {\n"
"font: italic 14pt \"Goudy Old Style\";\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"border-style : inset;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(14, 54, 61);\n"
"color:rgb(255,212,93);\n"
"}\n"
"")
        self.RequestsWidget.addWidget(self.Deposit_request_page)
        self.transfer_request_btn = QPushButton(self.Approval_message_page)
        self.transfer_request_btn.setObjectName(u"transfer_request_btn")
        self.transfer_request_btn.setGeometry(QRect(50, 40, 181, 41))
        self.transfer_request_btn.setStyleSheet(u"QPushButton {\n"
"font: italic 14pt \"Goudy Old Style\";\n"
"background-color:rgb(14, 54, 61);\n"
"color:rgb(255,212,93);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"border-style : inset;\n"
"}\n"
"QPushButton:hover {\n"
"\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"}\n"
"")
        self.deposit_request_btn = QPushButton(self.Approval_message_page)
        self.deposit_request_btn.setObjectName(u"deposit_request_btn")
        self.deposit_request_btn.setGeometry(QRect(310, 40, 181, 41))
        self.deposit_request_btn.setStyleSheet(u"QPushButton {\n"
"font: italic 14pt \"Goudy Old Style\";\n"
"background-color:rgb(14, 54, 61);\n"
"color:rgb(255,212,93);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"border-style : inset;\n"
"}\n"
"QPushButton:hover {\n"
"\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.Approval_message_page)
        self.Transaction_history_page = QWidget()
        self.Transaction_history_page.setObjectName(u"Transaction_history_page")
        self.Transactions_history_table = QTableWidget(self.Transaction_history_page)
        self.Transactions_history_table.setObjectName(u"Transactions_history_table")
        self.Transactions_history_table.setGeometry(QRect(20, 100, 491, 221))
        self.Transactions_history_table.setStyleSheet(u"font: 75 14pt \"Goudy Old Style\";\n"
"color: rgb(0, 0, 0);")
        self.label_13 = QLabel(self.Transaction_history_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(130, 20, 251, 41))
        self.label_13.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 16pt \"Goudy Old Style\";")
        self.stackedWidget.addWidget(self.Transaction_history_page)
        self.Transfe_page = QWidget()
        self.Transfe_page.setObjectName(u"Transfe_page")
        self.Transfer_check_widget = QStackedWidget(self.Transfe_page)
        self.Transfer_check_widget.setObjectName(u"Transfer_check_widget")
        self.Transfer_check_widget.setGeometry(QRect(20, 70, 481, 251))
        self.Account_verify_page = QWidget()
        self.Account_verify_page.setObjectName(u"Account_verify_page")
        self.label_15 = QLabel(self.Account_verify_page)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 40, 231, 41))
        self.label_15.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 16pt \"Goudy Old Style\";")
        self.limit_edt_2 = QLineEdit(self.Account_verify_page)
        self.limit_edt_2.setObjectName(u"limit_edt_2")
        self.limit_edt_2.setGeometry(QRect(250, 50, 171, 31))
        self.limit_edt_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.verify_acc_btn = QPushButton(self.Account_verify_page)
        self.verify_acc_btn.setObjectName(u"verify_acc_btn")
        self.verify_acc_btn.setGeometry(QRect(120, 120, 201, 41))
        self.verify_acc_btn.setStyleSheet(u"QPushButton {\n"
"font: italic 14pt \"Goudy Old Style\";\n"
"background-color:rgb(14, 54, 61);\n"
"color:rgb(255,212,93);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"border-style : inset;\n"
"}\n"
"QPushButton:hover {\n"
"\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"}\n"
"")
        self.Transfer_check_widget.addWidget(self.Account_verify_page)
        self.Amount_enter_page = QWidget()
        self.Amount_enter_page.setObjectName(u"Amount_enter_page")
        self.Confirm_amnt_btn = QPushButton(self.Amount_enter_page)
        self.Confirm_amnt_btn.setObjectName(u"Confirm_amnt_btn")
        self.Confirm_amnt_btn.setGeometry(QRect(160, 200, 201, 41))
        self.Confirm_amnt_btn.setStyleSheet(u"QPushButton {\n"
"font: italic 14pt \"Goudy Old Style\";\n"
"background-color:rgb(14, 54, 61);\n"
"color:rgb(255,212,93);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"border-style : inset;\n"
"}\n"
"QPushButton:hover {\n"
"\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"}\n"
"")
        self.label_16 = QLabel(self.Amount_enter_page)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(100, 40, 101, 21))
        self.label_16.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 16pt \"Goudy Old Style\";")
        self.label_17 = QLabel(self.Amount_enter_page)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(100, 80, 101, 21))
        self.label_17.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 16pt \"Goudy Old Style\";")
        self.label_18 = QLabel(self.Amount_enter_page)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(100, 120, 171, 21))
        self.label_18.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 16pt \"Goudy Old Style\";")
        self.Name_edt = QLineEdit(self.Amount_enter_page)
        self.Name_edt.setObjectName(u"Name_edt")
        self.Name_edt.setGeometry(QRect(280, 40, 151, 21))
        self.Name_edt.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.Amount_edt = QLineEdit(self.Amount_enter_page)
        self.Amount_edt.setObjectName(u"Amount_edt")
        self.Amount_edt.setGeometry(QRect(280, 80, 151, 21))
        self.Amount_edt.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.re_amnt_edt = QLineEdit(self.Amount_enter_page)
        self.re_amnt_edt.setObjectName(u"re_amnt_edt")
        self.re_amnt_edt.setGeometry(QRect(280, 120, 151, 21))
        self.re_amnt_edt.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_21 = QLabel(self.Amount_enter_page)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(100, 160, 171, 21))
        self.label_21.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 16pt \"Goudy Old Style\";")
        self.re_amnt_edt_2 = QLineEdit(self.Amount_enter_page)
        self.re_amnt_edt_2.setObjectName(u"re_amnt_edt_2")
        self.re_amnt_edt_2.setGeometry(QRect(280, 160, 151, 21))
        self.re_amnt_edt_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.Transfer_check_widget.addWidget(self.Amount_enter_page)
        self.final_check_page = QWidget()
        self.final_check_page.setObjectName(u"final_check_page")
        self.usernm_edt = QLineEdit(self.final_check_page)
        self.usernm_edt.setObjectName(u"usernm_edt")
        self.usernm_edt.setGeometry(QRect(250, 60, 151, 21))
        self.usernm_edt.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.pass_Edt = QLineEdit(self.final_check_page)
        self.pass_Edt.setObjectName(u"pass_Edt")
        self.pass_Edt.setGeometry(QRect(250, 100, 151, 21))
        self.pass_Edt.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_19 = QLabel(self.final_check_page)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(120, 50, 101, 41))
        self.label_19.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 16pt \"Goudy Old Style\";")
        self.label_20 = QLabel(self.final_check_page)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(120, 90, 101, 41))
        self.label_20.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 16pt \"Goudy Old Style\";")
        self.transfer_money_btn = QPushButton(self.final_check_page)
        self.transfer_money_btn.setObjectName(u"transfer_money_btn")
        self.transfer_money_btn.setGeometry(QRect(160, 160, 201, 41))
        self.transfer_money_btn.setStyleSheet(u"QPushButton {\n"
"font: italic 14pt \"Goudy Old Style\";\n"
"background-color:rgb(14, 54, 61);\n"
"color:rgb(255,212,93);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"border-style : inset;\n"
"}\n"
"QPushButton:hover {\n"
"\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"}\n"
"")
        self.Transfer_check_widget.addWidget(self.final_check_page)
        self.label_14 = QLabel(self.Transfe_page)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(190, 20, 141, 41))
        self.label_14.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 20pt \"Goudy Old Style\";")
        self.stackedWidget.addWidget(self.Transfe_page)
        self.Addmoney_page = QWidget()
        self.Addmoney_page.setObjectName(u"Addmoney_page")
        self.label_22 = QLabel(self.Addmoney_page)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(40, 130, 241, 41))
        self.label_22.setStyleSheet(u"background-color: rgb(255, 210, 93);\n"
"color: rgb(21, 84, 93);\n"
"font: 75 18pt \"Goudy Old Style\";\n"
" ")
        self.deposit_btn_child = QPushButton(self.Addmoney_page)
        self.deposit_btn_child.setObjectName(u"deposit_btn_child")
        self.deposit_btn_child.setGeometry(QRect(160, 210, 201, 41))
        self.deposit_btn_child.setStyleSheet(u"QPushButton {\n"
"font: italic 14pt \"Goudy Old Style\";\n"
"background-color:rgb(14, 54, 61);\n"
"color:rgb(255,212,93);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"border-style : inset;\n"
"}\n"
"QPushButton:hover {\n"
"\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"}\n"
"")
        self.Deposit_amnt_edt = QLineEdit(self.Addmoney_page)
        self.Deposit_amnt_edt.setObjectName(u"Deposit_amnt_edt")
        self.Deposit_amnt_edt.setGeometry(QRect(330, 140, 141, 21))
        self.label_2 = QLabel(self.Addmoney_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 50, 171, 61))
        self.label_2.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 22pt \"Goudy Old Style\";")
        self.label_2.setIndent(8)
        self.stackedWidget.addWidget(self.Addmoney_page)
        self.Transaction_limit_page = QWidget()
        self.Transaction_limit_page.setObjectName(u"Transaction_limit_page")
        self.label_11 = QLabel(self.Transaction_limit_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(100, 20, 311, 41))
        self.label_11.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 16pt \"Goudy Old Style\";")
        self.label_12 = QLabel(self.Transaction_limit_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(80, 140, 141, 41))
        self.label_12.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 16pt \"Goudy Old Style\";")
        self.limit_edt = QLineEdit(self.Transaction_limit_page)
        self.limit_edt.setObjectName(u"limit_edt")
        self.limit_edt.setGeometry(QRect(240, 150, 171, 31))
        self.limit_edt.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.set_lmt_btn = QPushButton(self.Transaction_limit_page)
        self.set_lmt_btn.setObjectName(u"set_lmt_btn")
        self.set_lmt_btn.setGeometry(QRect(140, 230, 201, 41))
        self.set_lmt_btn.setStyleSheet(u"QPushButton {\n"
"font: italic 14pt \"Goudy Old Style\";\n"
"background-color:rgb(14, 54, 61);\n"
"color:rgb(255,212,93);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"border-style : inset;\n"
"}\n"
"QPushButton:hover {\n"
"\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.Transaction_limit_page)
        self.logout_btn = QPushButton(self.centralwidget)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setGeometry(QRect(650, 10, 91, 31))
        self.logout_btn.setStyleSheet(u"QPushButton {\n"
"font: italic 14pt \"Goudy Old Style\";\n"
"background-color:rgb(14, 54, 61);\n"
"color:rgb(255,212,93);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"border-style : inset;\n"
"}\n"
"QPushButton:hover {\n"
"\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"}\n"
"")
        self.Ad_money_btn = QPushButton(self.centralwidget)
        self.Ad_money_btn.setObjectName(u"Ad_money_btn")
        self.Ad_money_btn.setGeometry(QRect(10, 190, 201, 41))
        self.Ad_money_btn.setStyleSheet(u"QPushButton {\n"
"font: italic 18pt \"Goudy Old Style\";\n"
"background-color: rgb(255, 212, 93);\n"
"color: rgb(21, 82, 93);\n"
"border: 1px solid;\n"
"border-radius: 15px;\n"
"border-style : inset;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(14, 54, 61);\n"
"color:rgb(255,212,93);\n"
"}\n"
"")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(250, 50, 231, 41))
        self.label_10.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 16pt \"Goudy Old Style\";")
        self.balance_lbl = QLabel(self.centralwidget)
        self.balance_lbl.setObjectName(u"balance_lbl")
        self.balance_lbl.setGeometry(QRect(490, 50, 151, 41))
        self.balance_lbl.setStyleSheet(u"color: rgb(21, 84, 93);\n"
"font: 75 16pt \"Goudy Old Style\";")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.RequestsWidget.setCurrentIndex(0)
        self.Transfer_check_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.Approval_btn.setText(QCoreApplication.translate("MainWindow", u"Approval Messages", None))
        self.transfer_btn.setText(QCoreApplication.translate("MainWindow", u"Transfer", None))
        self.transaction_btn.setText(QCoreApplication.translate("MainWindow", u"Transaction History", None))
        self.transaction_lmt_btn.setText(QCoreApplication.translate("MainWindow", u"Edit transaction limit", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Parent Account Number :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Biijjju", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"9638527445", None))
        self.approve_transaction_btn.setText(QCoreApplication.translate("MainWindow", u"Approve", None))
        self.deny_transaction_btn.setText(QCoreApplication.translate("MainWindow", u"Deny", None))
        self.approve_deposit_btn.setText(QCoreApplication.translate("MainWindow", u"Approve", None))
        self.deny_deposit_btn.setText(QCoreApplication.translate("MainWindow", u"Deny", None))
        self.transfer_request_btn.setText(QCoreApplication.translate("MainWindow", u"Transfer Requests", None))
        self.deposit_request_btn.setText(QCoreApplication.translate("MainWindow", u"Deposit Requests", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TRANSACTION HISTORY", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Enter Account Number :", None))
        self.verify_acc_btn.setText(QCoreApplication.translate("MainWindow", u"Verify", None))
        self.Confirm_amnt_btn.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Amount :", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Re-enter Amount :", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Message :", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Username :", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Password :", None))
        self.transfer_money_btn.setText(QCoreApplication.translate("MainWindow", u"Transfer", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"TRANSFER", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Enter Amount", None))
        self.deposit_btn_child.setText(QCoreApplication.translate("MainWindow", u"Add Money", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Add Money", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"SET NEW TRANSACTION LIMIT", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Enter Amount :", None))
        self.set_lmt_btn.setText(QCoreApplication.translate("MainWindow", u"Set limit", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.Ad_money_btn.setText(QCoreApplication.translate("MainWindow", u"Add money", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Account Balance  :", None))
        self.balance_lbl.setText(QCoreApplication.translate("MainWindow", u"9638527445", None))
    # retranslateUi

