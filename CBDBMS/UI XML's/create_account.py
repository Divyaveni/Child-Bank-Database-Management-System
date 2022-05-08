# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_account.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(727, 566)
        MainWindow.setStyleSheet("background-color: rgb(21, 84, 93);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 0, 131, 121))
        self.label.setStyleSheet("background-image: url(:/assets/logo3_1.png);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/assets/logo3_1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.transaction_btn = QtWidgets.QPushButton(self.centralwidget)
        self.transaction_btn.setGeometry(QtCore.QRect(40, 50, 231, 41))
        self.transaction_btn.setStyleSheet("QPushButton {\n"
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
        self.transaction_btn.setObjectName("transaction_btn")
        self.transaction_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.transaction_btn_2.setGeometry(QtCore.QRect(480, 50, 231, 41))
        self.transaction_btn_2.setStyleSheet("QPushButton {\n"
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
        self.transaction_btn_2.setObjectName("transaction_btn_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 150, 721, 411))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Home_page = QtWidgets.QWidget()
        self.Home_page.setObjectName("Home_page")
        self.label_15 = QtWidgets.QLabel(self.Home_page)
        self.label_15.setGeometry(QtCore.QRect(230, 30, 291, 71))
        self.label_15.setStyleSheet("font: 75 22pt \"Goudy Old Style\";\n"
"color: rgb(255, 212, 93);")
        self.label_15.setObjectName("label_15")
        self.stackedWidget.addWidget(self.Home_page)
        self.Parent_page = QtWidgets.QWidget()
        self.Parent_page.setObjectName("Parent_page")
        self.label_2 = QtWidgets.QLabel(self.Parent_page)
        self.label_2.setGeometry(QtCore.QRect(80, 80, 91, 21))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.Parent_page)
        self.label_4.setGeometry(QtCore.QRect(80, 130, 151, 21))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.Parent_page)
        self.label_5.setGeometry(QtCore.QRect(80, 170, 91, 21))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.Parent_page)
        self.label_6.setGeometry(QtCore.QRect(80, 220, 91, 21))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.Parent_page)
        self.label_7.setGeometry(QtCore.QRect(80, 270, 151, 21))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_7.setObjectName("label_7")
        self.Name_edt = QtWidgets.QLineEdit(self.Parent_page)
        self.Name_edt.setGeometry(QtCore.QRect(460, 70, 191, 31))
        self.Name_edt.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.Name_edt.setObjectName("Name_edt")
        self.phone_edt = QtWidgets.QLineEdit(self.Parent_page)
        self.phone_edt.setGeometry(QtCore.QRect(460, 120, 191, 31))
        self.phone_edt.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.phone_edt.setObjectName("phone_edt")
        self.username_edt = QtWidgets.QLineEdit(self.Parent_page)
        self.username_edt.setGeometry(QtCore.QRect(460, 170, 191, 31))
        self.username_edt.setObjectName("username_edt")
        self.pass_edit = QtWidgets.QLineEdit(self.Parent_page)
        self.pass_edit.setGeometry(QtCore.QRect(460, 210, 191, 31))
        self.pass_edit.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.pass_edit.setObjectName("pass_edit")
        self.repass_edt = QtWidgets.QLineEdit(self.Parent_page)
        self.repass_edt.setGeometry(QtCore.QRect(460, 250, 191, 31))
        self.repass_edt.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.repass_edt.setObjectName("repass_edt")
        self.label_8 = QtWidgets.QLabel(self.Parent_page)
        self.label_8.setGeometry(QtCore.QRect(260, 10, 221, 21))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 24pt \"Goudy Old Style\";")
        self.label_8.setObjectName("label_8")
        self.Submit_btn = QtWidgets.QPushButton(self.Parent_page)
        self.Submit_btn.setGeometry(QtCore.QRect(270, 360, 181, 31))
        self.Submit_btn.setStyleSheet("QPushButton {\n"
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
        self.Submit_btn.setObjectName("Submit_btn")
        self.label_3 = QtWidgets.QLabel(self.Parent_page)
        self.label_3.setGeometry(QtCore.QRect(80, 310, 91, 21))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_3.setObjectName("label_3")
        self.Email_edt = QtWidgets.QLineEdit(self.Parent_page)
        self.Email_edt.setGeometry(QtCore.QRect(460, 290, 191, 31))
        self.Email_edt.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.Email_edt.setObjectName("Email_edt")
        self.stackedWidget.addWidget(self.Parent_page)
        self.Child_page = QtWidgets.QWidget()
        self.Child_page.setObjectName("Child_page")
        self.label_9 = QtWidgets.QLabel(self.Child_page)
        self.label_9.setGeometry(QtCore.QRect(280, 30, 191, 21))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 24pt \"Goudy Old Style\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.Child_page)
        self.label_10.setGeometry(QtCore.QRect(120, 290, 151, 21))
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.Child_page)
        self.label_11.setGeometry(QtCore.QRect(120, 250, 91, 21))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.Child_page)
        self.label_12.setGeometry(QtCore.QRect(120, 80, 91, 21))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_12.setObjectName("label_12")
        self.child_username_edt = QtWidgets.QLineEdit(self.Child_page)
        self.child_username_edt.setGeometry(QtCore.QRect(430, 160, 191, 31))
        self.child_username_edt.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.child_username_edt.setObjectName("child_username_edt")
        self.child_parent_Acc_edt = QtWidgets.QLineEdit(self.Child_page)
        self.child_parent_Acc_edt.setGeometry(QtCore.QRect(430, 200, 191, 31))
        self.child_parent_Acc_edt.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.child_parent_Acc_edt.setObjectName("child_parent_Acc_edt")
        self.label_13 = QtWidgets.QLabel(self.Child_page)
        self.label_13.setGeometry(QtCore.QRect(120, 170, 91, 21))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_13.setObjectName("label_13")
        self.child_repass_edt = QtWidgets.QLineEdit(self.Child_page)
        self.child_repass_edt.setGeometry(QtCore.QRect(430, 280, 191, 31))
        self.child_repass_edt.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.child_repass_edt.setObjectName("child_repass_edt")
        self.child_Name_edt = QtWidgets.QLineEdit(self.Child_page)
        self.child_Name_edt.setGeometry(QtCore.QRect(430, 70, 191, 31))
        self.child_Name_edt.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.child_Name_edt.setObjectName("child_Name_edt")
        self.label_14 = QtWidgets.QLabel(self.Child_page)
        self.label_14.setGeometry(QtCore.QRect(120, 130, 131, 21))
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_14.setObjectName("label_14")
        self.dateEdit = QtWidgets.QDateEdit(self.Child_page)
        self.dateEdit.setGeometry(QtCore.QRect(430, 120, 191, 31))
        self.dateEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.dateEdit.setObjectName("dateEdit")
        self.child_submit_btn = QtWidgets.QPushButton(self.Child_page)
        self.child_submit_btn.setGeometry(QtCore.QRect(280, 370, 181, 31))
        self.child_submit_btn.setStyleSheet("QPushButton {\n"
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
        self.child_submit_btn.setObjectName("child_submit_btn")
        self.child_pass_edt = QtWidgets.QLineEdit(self.Child_page)
        self.child_pass_edt.setGeometry(QtCore.QRect(430, 240, 191, 31))
        self.child_pass_edt.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.child_pass_edt.setObjectName("child_pass_edt")
        self.label_16 = QtWidgets.QLabel(self.Child_page)
        self.label_16.setGeometry(QtCore.QRect(120, 210, 221, 21))
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.Child_page)
        self.label_17.setGeometry(QtCore.QRect(120, 330, 151, 21))
        self.label_17.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.label_17.setObjectName("label_17")
        self.child_mail_edt = QtWidgets.QLineEdit(self.Child_page)
        self.child_mail_edt.setGeometry(QtCore.QRect(430, 320, 191, 31))
        self.child_mail_edt.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Goudy Old Style\";")
        self.child_mail_edt.setObjectName("child_mail_edt")
        self.stackedWidget.addWidget(self.Child_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.transaction_btn.setText(_translate("MainWindow", "Create Account Parent"))
        self.transaction_btn_2.setText(_translate("MainWindow", "Create Account Child"))
        self.label_15.setText(_translate("MainWindow", "Welcome To Balya Bank"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "Phone Number"))
        self.label_5.setText(_translate("MainWindow", "Username"))
        self.label_6.setText(_translate("MainWindow", "Password"))
        self.label_7.setText(_translate("MainWindow", "Re-enter Password"))
        self.label_8.setText(_translate("MainWindow", "Parent Account"))
        self.Submit_btn.setText(_translate("MainWindow", "Submit"))
        self.label_3.setText(_translate("MainWindow", "Email ID"))
        self.label_9.setText(_translate("MainWindow", "Child Account"))
        self.label_10.setText(_translate("MainWindow", "Re-enter Password"))
        self.label_11.setText(_translate("MainWindow", "Password"))
        self.label_12.setText(_translate("MainWindow", "Name"))
        self.label_13.setText(_translate("MainWindow", "Username"))
        self.label_14.setText(_translate("MainWindow", "Date Of Birth"))
        self.child_submit_btn.setText(_translate("MainWindow", "Submit"))
        self.label_16.setText(_translate("MainWindow", "Parent Account Number"))
        self.label_17.setText(_translate("MainWindow", "Email Id"))
import com_logo_rc