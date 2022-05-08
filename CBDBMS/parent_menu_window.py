import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)

from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from UI.ui_Parent_display import *
from Functions.transaction import *

from UI.msg_dialog import Ui_Dialog

class Parent_MainWindow:
    def __init__(self,Account_number,Name,Balance):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.Approval_message_page)
        self.ui.RequestsWidget.setCurrentWidget(self.ui.Transfer_request_page)
        self.Account_number = Account_number
        self.Balance = Balance
        self.Name = Name
        self.child_acc = ""
        self.child_user = ""

        self.ui.balance_lbl.setText("Rs."+str(Balance))
        
        self.dialogue_win = QDialog()
        self.dialog_ui = Ui_Dialog()
        self.dialog_ui.setupUi(self.dialogue_win)        
        
        self.ui.label_9.setText(str(self.Account_number))
        self.ui.label_8.setText(str(self.Name))
       
        
        #button_actions
        self.ui.Approval_btn.clicked.connect(self.approval_page_display)
        self.ui.transfer_btn.clicked.connect(self.transfer_page_display)
        self.ui.transaction_btn.clicked.connect(self.transaction_page_display)
        self.ui.transaction_lmt_btn.clicked.connect(self.transaction_limit_display)
        
        self.ui.transfer_request_btn.clicked.connect(self.show_transfer_requests_page)
        self.ui.deposit_request_btn.clicked.connect(self.show_deposit_requests_page)
        self.ui.Ad_money_btn.clicked.connect(self.show_add_page)
        
        self.ui.approve_transaction_btn.clicked.connect(self.approve_transaction_page)
        
        #transaction_requests
        self.ui.transfer_request_table.setRowCount(100);
        self.ui.transfer_request_table.setColumnCount(6);
        self.columnLabels = ["Request Id","UserName","Child Account Number","Amount","Credit Account","Message"]
        self.ui.transfer_request_table.setHorizontalHeaderLabels(self.columnLabels)
        
        self.ui.Transactions_history_table.setRowCount(100);
        self.ui.Transactions_history_table.setColumnCount(5);
        
        # transaction History
        self.columnLabels = ["Date","Transaction Id","Amount","Transaction type","message"]
        success,to_child,from_child = transactions_by_child_from_parent(int(self.Account_number))
        row_2 = 0
        for each_to_child in to_child:
            transaction_at = QTableWidgetItem(str(each_to_child['transactionAt']))
            transaction_id = QTableWidgetItem(str(each_to_child['transaction_id']))
            Amount = QTableWidgetItem(str(each_to_child['amount']))
            Transaction_type = QTableWidgetItem("Credit")
            msg = QTableWidgetItem("Credited from "+str(each_to_child['from_account_number']))
            self.ui.Transactions_history_table.setItem(row_2,0,transaction_at)
            self.ui.Transactions_history_table.setItem(row_2,1,transaction_id)
            self.ui.Transactions_history_table.setItem(row_2,2,Amount)
            self.ui.Transactions_history_table.setItem(row_2,3,Transaction_type)
            self.ui.Transactions_history_table.setItem(row_2,4,msg)
            row_2 = row_2 + 1
            
        for each_to_child in from_child:
            transaction_at = QTableWidgetItem(str(each_to_child['transactionAt']))
            transaction_id = QTableWidgetItem(str(each_to_child['transaction_id']))
            Amount = QTableWidgetItem(str(each_to_child['amount']))
            Transaction_type = QTableWidgetItem("Debit")
            msg = QTableWidgetItem("debitted from "+str(each_to_child['from_account_number']))
            self.ui.Transactions_history_table.setItem(row_2,0,transaction_at)
            self.ui.Transactions_history_table.setItem(row_2,1,transaction_id)
            self.ui.Transactions_history_table.setItem(row_2,2,Amount)
            self.ui.Transactions_history_table.setItem(row_2,3,Transaction_type)
            self.ui.Transactions_history_table.setItem(row_2,4,msg)
            row_2 = row_2 + 1        
        self.ui.Transactions_history_table.setHorizontalHeaderLabels(self.columnLabels)
        self.ui.Transactions_history_table.resizeColumnsToContents()
        
        
        # Transfer requests
        success,requests_child = transactions_request_child_from_parent(int(self.Account_number))
        row = 0
        for request_each in requests_child:
            if str(request_each['type']) == "transfer":
                tran_id = QTableWidgetItem(str(request_each['transaction_request_id']))
                name = QTableWidgetItem(str(request_each['child_username']))
                child_acc = QTableWidgetItem(str(request_each['child_account_number']))
                amnt = QTableWidgetItem(str(request_each['amount']))
                to_acc = QTableWidgetItem(str(request_each['toAcc']))
                message = QTableWidgetItem(str(request_each['message']))
                self.ui.transfer_request_table.setItem(row,0,tran_id)
                self.ui.transfer_request_table.setItem(row,1,name)
                self.ui.transfer_request_table.setItem(row,2,child_acc)
                self.ui.transfer_request_table.setItem(row,3,amnt)
                self.ui.transfer_request_table.setItem(row,4,to_acc)
                self.ui.transfer_request_table.setItem(row,5,message)
                row = row+1
        self.ui.transfer_request_table.resizeColumnsToContents()
        
        #deposit requests
        success,requests_child_2 = transactions_request_child_from_parent(int(self.Account_number))
        self.ui.deposit_requests_table.setRowCount(100);
        self.ui.deposit_requests_table.setColumnCount(6);
        self.columnLabels_deposit = ["Request Id","UserName","Child Account Number","Amount","Credit Account","Message"]
        self.ui.deposit_requests_table.setHorizontalHeaderLabels(self.columnLabels_deposit)
        row_1 = 0
        for request_each in requests_child_2:
            if str(request_each['type']) == "deposit":
                tran_id = QTableWidgetItem(str(request_each['transaction_request_id']))
                name = QTableWidgetItem(str(request_each['child_username']))
                child_acc = QTableWidgetItem(str(request_each['child_account_number']))
                amnt = QTableWidgetItem(str(request_each['amount']))
                to_acc = QTableWidgetItem(str(request_each['toAcc']))
                message = QTableWidgetItem(str(request_each['message']))
                self.ui.deposit_requests_table.setItem(row_1,0,tran_id)
                self.ui.deposit_requests_table.setItem(row_1,1,name)
                self.ui.deposit_requests_table.setItem(row_1,2,child_acc)
                self.ui.deposit_requests_table.setItem(row_1,3,amnt)
                self.ui.deposit_requests_table.setItem(row_1,4,to_acc)
                self.ui.deposit_requests_table.setItem(row_1,5,message)
                row_1 = row_1+1
        self.ui.deposit_requests_table.resizeColumnsToContents()
        
        self.ui.approve_deposit_btn.clicked.connect(self.approve_deposit)
        
            
            
             
       
    def show(self):
        self.main_win.show()
    
    def approve_deposit(self):
        row = self.ui.deposit_requests_table.currentRow()
        to_acc = self.ui.deposit_requests_table.item(row,4).text()
        amount = self.ui.deposit_requests_table.item(row, 3).text()
        Transaction_id = self.ui.deposit_requests_table.item(row, 0).text()
        success,messages = child_deposit(int(to_acc),int(amount))
        if success:
            self.dialog_ui.message_lbl.setText(str(messages))
            self.dialogue_win.show()
            self.ui.deposit_requests_table.removeRow(row)
            success,message = delete_transaction_request(int(Transaction_id))
            print(success)
        else:
            self.dialog_ui.message_lbl.setText(str(messages))
            self.dialogue_win.show()                
    
    def show_add_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Addmoney_page)
    def approval_page_display(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Approval_message_page)
    def transfer_page_display(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Transfe_page)
    def transaction_page_display(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Transaction_history_page)
    def transaction_limit_display(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Transaction_limit_page)
    def show_transfer_requests_page(self):
        self.ui.RequestsWidget.setCurrentWidget(self.ui.Transfer_request_page)
    def show_deposit_requests_page(self):
        self.ui.RequestsWidget.setCurrentWidget(self.ui.Deposit_request_page)
    def approve_transaction_page(self):
        row = self.ui.transfer_request_table.currentRow()
        Transaction_id = self.ui.transfer_request_table.item(row, 0).text()
        username = self.ui.transfer_request_table.item(row, 1).text()
        amount = self.ui.transfer_request_table.item(row, 3).text()
        from_acc = self.ui.transfer_request_table.item(row,2).text()
        to_acc = self.ui.transfer_request_table.item(row,4).text()
        message = self.ui.transfer_request_table.item(row,5).text()
        approved_by = self.Account_number
        
        success,message = child_transaction(username,int(amount),int(from_acc),int(to_acc),int(approved_by),message) 
        if success:
            self.dialog_ui.message_lbl.setText(str(Transaction_id)+str(message))
            self.dialogue_win.show()
            self.ui.transfer_request_table.removeRow(row)
            success,message = delete_transaction_request(int(Transaction_id))
            print(success)
        else:
            self.dialog_ui.message_lbl.setText(str(message))
            self.dialogue_win.show()            
        
