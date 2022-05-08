import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)

from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from UI.ui_create_account import Create_account
from Functions.signup import *
from parent_Login import ParentLoginWindow, ChildLoginWindow

# from main import MainWindow

class CreateAccountWindow:
    def __init__(self):
        self.main_win = QWidget()
        self.ui = Create_account()
        self.ui.setupUi(self.main_win)
        self.parent_window = ParentLoginWindow()
        self.child_window = ChildLoginWindow()
        self.ui.Submit_btn.clicked.connect(self.parentSignup)
        self.ui.child_submit_btn.clicked.connect(self.childsignup)
        self.ui.transaction_btn.clicked.connect(self.show_parent_account_create)
        self.ui.transaction_btn_2.clicked.connect(self.show_child_account_create)
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home_page)
        
        self.ui.Back_btn.clicked.connect(self.back_fun)
    
    def back_fun(self):
        pass
        
        
        
    def show_parent_account_create(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Parent_page)
    def show_child_account_create(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Child_page)
    
    def parentSignup(self):
        if self.ui.pass_edit.text() == self.ui.repass_edt.text():
            parent_signup_success = parent_signup(self.ui.Name_edt.text(), self.ui.username_edt.text(),self.ui.pass_edit.text(), self.ui.phone_edt.text(),self.ui.Email_edt.text())
            if parent_signup_success:
                self.parent_window.show()
                self.main_win.hide()
    
    def childsignup(self):
        print("yes1")
        if self.ui.child_pass_edt.text() == self.ui.child_repass_edt.text():
            child_signup_success = child_signup(self.ui.child_Name_edt.text(),self.ui.child_username_edt.text(),self.ui.child_pass_edt.text(),self.ui.child_parent_Acc_edt.text(),self.ui.dateEdit.text(),self.ui.child_mail_edt.text())
            if child_signup_success:
                print("yes2")
                self.child_window.show()
                self.main_win.hide()
                
                
    def show(self):
        self.main_win.show()

