import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)

from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from Functions.login import *

from UI.ui_Parent_Login import Parent_Login
from UI.ui_Parent_display import Ui_MainWindow
from parent_menu_window import Parent_MainWindow
from UI.ui_Child_login import Child_login
from child_menu_window import Child_Main_window
from UI.msg_dialog import Ui_Dialog


class ParentLoginWindow:
    def __init__(self):
        self.main_win = QWidget()
        self.ui = Parent_Login()
        self.ui.setupUi(self.main_win)
        
        
        self.dialogue_win = QDialog()
        self.dialog_ui = Ui_Dialog()
        self.dialog_ui.setupUi(self.dialogue_win)
        
        self.ui.Login_btn.clicked.connect(self.parentLoginCheck)
        
    def parentLoginCheck(self):
        success,parent_details = parent_login(self.ui.lineEdit.text(),self.ui.lineEdit_2.text())
        if success:
            self.parentdisplay = Parent_MainWindow(parent_details['account_number'],parent_details['name'],parent_details['balance'])
            self.parentdisplay.show()
            self.main_win.hide()
        else:
            self.dialog_ui.message_lbl.setText("Invalid Credetials")
            self.dialogue_win.show()

        
    def show(self):
        self.main_win.show()


 
class ChildLoginWindow:
    def __init__(self):
        self.main_win = QWidget()
        self.ui = Child_login()
        self.ui.setupUi(self.main_win)
        
        self.dialogue_win = QDialog()
        self.dialog_ui = Ui_Dialog()
        self.dialog_ui.setupUi(self.dialogue_win)
        
        
        self.ui.pushButton.clicked.connect(self.childLoginCheck)

    def childLoginCheck(self):
        success,details = child_login(self.ui.lineEdit.text(),self.ui.lineEdit_2.text())
        
        if success:
            self.childdisplay = Child_Main_window(details['account_number'],details['name'],details['balance'],details['username'])
            self.childdisplay.show()
            self.main_win.hide()
        else:
            self.dialog_ui.message_lbl.setText("Invalid Credetials")
            self.dialogue_win.show()
            
        
    def show(self):
        self.main_win.show()   
 
 
 
 
 
 
 
 
 
 
 
 

