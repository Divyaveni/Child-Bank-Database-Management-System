import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)

from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from UI.ui_Child_menu_page import *
from Functions.transaction import *
from UI.msg_dialog import Ui_Dialog

class Child_Main_window:
    def __init__(self,Account_number,Name,Balance,username):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.Account_number = Account_number
        self.Name = Name
        self.Balance = Balance
        self.username = username
        self.to_acc = ""
        
        #dialogue
        self.dialogue_win = QDialog()
        self.dialog_ui = Ui_Dialog()
        self.dialog_ui.setupUi(self.dialogue_win)
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.transaction_page)
        self.ui.transaction_btn.clicked.connect(self.show_transaction_page)
        self.ui.transfer_btn.clicked.connect(self.show_transfer_page)
        self.ui.deposit_btn.clicked.connect(self.show_deposit_page)
        
        
        self.ui.deposit_btn_child.clicked.connect(self.depositAmount)
        self.ui.verify_btn.clicked.connect(self.verify_account_number)
        
        self.ui.deposit_btn_child.clicked.connect(self.depostit_request)
        
        self.ui.label_2.setText(self.Name)
        self.ui.label_17.setText(str(self.Account_number))
        self.ui.label_8.setText(str(self.Balance))
                
        self.ui.Transfer_widget.setCurrentWidget(self.ui.verify_account_page)
        
        self.ui.History_table.setRowCount(100);
        self.ui.History_table.setColumnCount(5);
        # transaction History
        self.columnLabels = ["Date","Transaction Id","Amount","Transaction type","message"]
        self.ui.History_table.setHorizontalHeaderLabels(self.columnLabels)
        success,to_child,from_child = transactions_by_child(self.username,int(self.Account_number))
        row_2 = 0
        for each_to_child in to_child:
            transaction_at = QTableWidgetItem(str(each_to_child['transactionAt']))
            transaction_id = QTableWidgetItem(str(each_to_child['transaction_id']))
            Amount = QTableWidgetItem(str(each_to_child['amount']))
            Transaction_type = QTableWidgetItem("Debit")
            msg = QTableWidgetItem("Debitted from "+str(each_to_child['from_account_number']))
            self.ui.History_table.setItem(row_2,0,transaction_at)
            self.ui.History_table.setItem(row_2,1,transaction_id)
            self.ui.History_table.setItem(row_2,2,Amount)
            self.ui.History_table.setItem(row_2,3,Transaction_type)
            self.ui.History_table.setItem(row_2,4,msg)
            row_2 = row_2 + 1
            
        for each_to_child in from_child:
            transaction_at = QTableWidgetItem(str(each_to_child['transactionAt']))
            transaction_id = QTableWidgetItem(str(each_to_child['transaction_id']))
            Amount = QTableWidgetItem(str(each_to_child['amount']))
            Transaction_type = QTableWidgetItem("Credit")
            msg = QTableWidgetItem("Creddited from "+str(each_to_child['from_account_number']))
            self.ui.History_table.setItem(row_2,0,transaction_at)
            self.ui.History_table.setItem(row_2,1,transaction_id)
            self.ui.History_table.setItem(row_2,2,Amount)
            self.ui.History_table.setItem(row_2,3,Transaction_type)
            self.ui.History_table.setItem(row_2,4,msg)
            row_2 = row_2 + 1        
        self.ui.History_table.resizeColumnsToContents()
        
        
        
        self.ui.confirm_btn.clicked.connect(self.show_Confirm_amount_page)
        self.ui.Transfer_btn.clicked.connect(self.transfer_request)
        
    
    
    def depostit_request(self):
        success,message = child_deposit_request(self.username,int(self.ui.Deposit_amnt_edt.text()),"good boy")
        if success:
            self.dialog_ui.message_lbl.setText(message)
            self.dialogue_win.show()
        else:
            self.dialog_ui.message_lbl.setText(message)
            self.dialogue_win.show()
    
    def transfer_request(self):
        success,success_message = child_transaction_request(self.ui.lineEdit.text(),self.ui.lineEdit_2.text(),int(self.ui.Name_edt_2.text()),int(self.ui.acc_edt.text()),self.ui.message_edt.text())
        if success:
            self.dialog_ui.message_lbl.setText(success_message)
            self.dialogue_win.show()
            self.ui.transaction_btn.setEnabled(True)
            self.ui.transfer_btn.setEnabled(True)
            self.ui.deposit_btn.setEnabled(True)
            self.ui.Transfer_widget.setCurrentWidget(self.ui.verify_account_page)
        else:
            self.dialog_ui.message_lbl.setText(success_message)
            self.dialogue_win.show()
    
    def depositAmount(self):
        success,message_success = child_deposit(int(self.Account_number),int(self.ui.Deposit_amnt_edt.text()))
        if success:
            self.dialog_ui.message_lbl.setText(message_success)
            self.dialogue_win.show()
        else:
            self.dialog_ui.message_lbl.setText(message_success)
            self.dialogue_win.show()
    
    def verify_account_number(self):
        success,details_of = verify_child_account(int(self.ui.acc_edt.text()))
        if success:
            self.ui.Transfer_widget.setCurrentWidget(self.ui.amount_enter_page)
            self.ui.transaction_btn.setEnabled(False)
            self.ui.transfer_btn.setEnabled(False)
            self.ui.deposit_btn.setEnabled(False)
            self.ui.Name_edt.setText(details_of["name"])
        else:
            self.dialog_ui.message_lbl.setText("Invalid Account Number")
            self.dialogue_win.show()        
        
    
    def show_amount_enter_page(self):
        self.ui.Transfer_widget.setCurrentWidget(self.ui.amount_enter_page)
    
    def show_Confirm_amount_page(self):
        self.ui.Transfer_widget.setCurrentWidget(self.ui.Confirm_amount_page)
    
    def show_transaction_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.transaction_page)
    def show_transfer_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.transfer_page)
    def show_deposit_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.depost_page)
    def show_withdraw_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.withdraw_page)
    
    def show(self):
        self.main_win.show()
