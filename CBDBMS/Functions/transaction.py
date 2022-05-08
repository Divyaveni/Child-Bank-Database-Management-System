import os
from datetime import datetime
from random import randint

import bcrypt
import smtplib
from dotenv import load_dotenv
from pymongo import MongoClient
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

# connect to DB
client = MongoClient(os.getenv("MONGODB"))

# DB references
db = client.cbdbms
parent_db = db.parent
child_db = db.child
transaction_db = db.transaction
transaction_request_db = db.transaction_request

child_daily_limit = 100


# Parent to some Account transaction
def parent_transaction(username, password, amount, to_account_number, to_account_type):
    try:
        # Get Parent Details
        parent_details = parent_db.find_one({"username": username})

        # Check password and check account type of recipient
        if bcrypt.checkpw(password.encode("utf-8"), parent_details["password"]) and (
                to_account_type == "child" or to_account_type == "parent"):
            # update from account balance
            if parent_details["balance"] >= amount:
                parent_details_update = {
                    "$set": {"balance": int(parent_details["balance"] - amount)}}
                parent_db.update_one(
                    {"username": username}, parent_details_update)

                # Update as Transaction
                transaction_db.create_index("transaction_id", unique=True)
                transaction_details = {
                    "username": username,
                    "from_account_number": parent_details["account_number"],
                    "to_account_number": to_account_number,
                    "transaction_id": randint(1, 1000000000000),
                    "transactionAt": datetime.now(),
                    "transaction_date": datetime.today(),
                    "amount": amount,
                    "to_type": to_account_type,
                    "by_type": "parent",
                    "transaction_type": "1to1"
                }
                print(parent_details_update)
                transaction_db.insert_one(transaction_details)

                if to_account_type == "parent":
                    # Get TO account Details
                    to_parent_details = parent_db.find_one(
                        {"account_number": to_account_number})
                    if bool(to_parent_details):
                        # Update TO account Balance
                        to_parent_details_update = {
                            "$set": {"balance": to_parent_details["balance"] + amount}}
                        parent_db.update_one(
                            {"account_number": to_account_number}, to_parent_details_update)
                    else:
                        return False, "account dose not exist"
                elif to_account_type == "child":
                    # Get TO account Details
                    to_child_details = child_db.find_one(
                        {"account_number": to_account_number})

                    if bool(to_child_details):
                        # Update TO account Balance
                        to_child_details_update = {
                            "$set": {"balance": to_child_details["balance"] + amount}}
                        child_db.update_one(
                            {"account_number": to_account_number}, to_child_details_update)
                    else:
                        return False, "account dose not exist"
                return True, "transaction success"
            else:
                return False, "insufficient balance"
        else:
            return False, "password incorrect"
    except Exception as e:
        print(e)
        return False, e


# Deposit to parent account
def parent_deposit(account_number, amount):
    try:
        # Get Parent Details
        parent_details = parent_db.find_one({"account_number": account_number})

        if bool(parent_details):
            # Update Parent Balance
            parent_details_update = {
                "$set": {"balance": parent_details["balance"] + amount}}
            parent_db.update_one(
                {"account_number": account_number}, parent_details_update)

            # Update as Transaction
            transaction_db.create_index("transaction_id", unique=True)
            transaction_details = {
                "username": parent_details["username"],
                "transaction_id": randint(1, 1000000000000),
                "transactionAt": datetime.now(),
                "transaction_date": datetime.today(),
                "amount": amount,
                "by_type": "parent",
                "transaction_type": "deposit"
            }
            transaction_db.insert_one(transaction_details)
            return True, "transaction success"
        else:
            return False, "account dose not exist"
    except Exception as e:
        print(e)
        return False, e


# Child transaction request
def child_deposit_request(username, amount, message):
    try:
        # Get child details
        child_details = child_db.find_one({"username": username})

        # check if password is correct
        transaction_request_id = randint(1, 1000000000000)
        transaction_request_db.create_index(
            "transaction_request_id", unique=True)
        transaction_request = {
            "child_username": username,
            "child_account_number": child_details["account_number"],
            "amount": amount,
            "message": message,
            "type": "deposit",
            "parent_account_number": child_details["parent_account_number"],
            "transaction_request_id": transaction_request_id,
            "toAcc": child_details["account_number"]
        }
        transaction_request_db.insert_one(transaction_request)

        parent_details = parent_db.find_one(
            {"account_number": child_details["parent_account_number"]})

        mail(parent_details, child_details, amount,
             child_details, transaction_request_id)

        return True, "transaction requested"

    except Exception as e:
        print(e)
        return False, "error"


def mail(parent_details, child_to_details, amount, child_details, transaction_request_id):
    sender_address = os.getenv("SMTP_EMAIL")
    sender_pass = os.getenv("SMTP_PASS")

    if child_details == child_to_details:
        mail_content = "To deposit amount of " + str(amount) + " to " + child_to_details[
            "name"] + " click on this link " + os.getenv(
            "SERVER_URL") + "/approve/" + str(transaction_request_id)

    else:
        mail_content = "To approve transaction amount of " + str(amount) + " by " + child_details[
            "name"] + " to " + child_to_details["name"] + " click on this link " + os.getenv(
            "SERVER_URL") + "/approve/" + str(transaction_request_id) + " and to reject transaction click on this link " + os.getenv(
            "SERVER_URL") + "/deny/" + str(transaction_request_id)

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = parent_details["email"]
    message['Subject'] = 'Approve transaction amount of ' + \
        str(amount) + "by" + child_details["name"]
    message.attach(MIMEText(mail_content, 'plain'))

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    session.sendmail(
        sender_address, parent_details["email"], message.as_string())


# Deposit to child account
def child_deposit(account_number, amount):
    try:
        # Get Child Details
        child_details = child_db.find_one({"account_number": account_number})

        if bool(child_details):
            parent_details = parent_db.find_one(
                {"account_number": child_details["parent_account_number"]})

            if amount > parent_details["balance"]:
                return False, "insufficient balance"

            balance_update = {
                "$set": {"balance": parent_details["balance"] - amount}}
            parent_db.update_one(
                {"username": parent_details["username"]}, balance_update)

            # Update Child Balance
            child_details_update = {
                "$set": {"balance": child_details["balance"] + amount}}
            child_db.update_one(
                {"account_number": account_number}, child_details_update)

            # Update as Transaction
            transaction_db.create_index("transaction_id", unique=True)
            transaction_details = {
                "username": child_details["username"],
                "transaction_id": randint(1, 1000000000000),
                "transactionAt": datetime.now(),
                "transaction_date": datetime.today(),
                "to_account_number": child_details["account_number"],
                "from_account_number": child_details["parent_account_number"],
                "amount": amount,
                "by_type": "child",
                "transaction_type": "deposit"
            }
            transaction_db.insert_one(transaction_details)

            return True, "transaction success"
        else:
            return False, "account dose not exist"
    except Exception as e:
        print(e)
        return False, e


# Child transaction request
def child_transaction_request(username, password, amount, to_acc, message):
    try:
        # Get child details
        child_details = child_db.find_one({"username": username})

        # check if password is correct
        if bcrypt.checkpw(password.encode("utf-8"), child_details["password"]):
            if child_details["balance"] >= amount:
                # check child's today's transactions
                child_today_transaction = transaction_db.find(
                    {"from_account_number": child_details["account_number"],
                        "transaction_date": datetime.today()}
                )
                amount_spent_today = 0
                for i in child_today_transaction:
                    amount_spent_today += i["amount"]

                    # if less than limit do transaction
                    return child_transaction(username, amount,
                                             child_details["account_number"], to_acc, "auto", message)
                else:
                    transaction_request_id = randint(1, 1000000000000)
                    # else make a transaction request
                    transaction_request_db.create_index(
                        "transaction_request_id", unique=True)
                    transaction_request = {
                        "child_username": username,
                        "child_account_number": child_details["account_number"],
                        "amount": amount,
                        "message": message,
                        "type": "transfer",
                        "parent_account_number": child_details["parent_account_number"],
                        "transaction_request_id": transaction_request_id,
                        "toAcc": to_acc
                    }
                    transaction_request_db.insert_one(transaction_request)

                    parent_details = parent_db.find_one(
                        {"account_number": child_details["parent_account_number"]})

                    child_to_details = child_db.find_one(
                        {"account_number": to_acc})

                    mail(parent_details, child_to_details, amount,
                         child_details, transaction_request_id)

                    return True, "transaction requested"
            else:
                return False, "insufficient balance"
        else:
            return False, "password incorrect"
    except Exception as e:
        print(e)
        return False, "error"


# Child transaction
def child_transaction(username, amount, from_acc, to_acc, approved_by, message):
    try:
        child_details = child_db.find_one(
            {"username": username, "account_number": int(from_acc)})
        balance_update = {"$set": {"balance": int(
            child_details["balance"]) - int(amount)}}
        child_db.update_one(
            {"username": username, "account_number": int(from_acc)}, balance_update)

        transaction_db.create_index("transaction_id", unique=True)
        transaction_details = {
            "username": username,
            "transaction_id": randint(1, 1000000000000),
            "transactionAt": datetime.now(),
            "amount": amount,
            "from_account_number": from_acc,
            "to_account_number": to_acc,
            "by_type": "child",
            "to_type": "child",
            "transaction_type": "1to1",
            "approved_by": approved_by,
            "message": message
        }
        transaction_db.insert_one(transaction_details)

        child_details = child_db.find_one({"account_number": to_acc})
        if bool(child_details):
            balance_update = {
                "$set": {"balance": child_details["balance"] + amount}}
            child_db.update_one(
                {"username": child_details["username"], "account_number": to_acc}, balance_update)
            return True, "transaction success"
        else:
            return False, "account dose not exist"
    except Exception as e:
        print(e)
        return False, e


# Verify if child account exists
def verify_child_account(account_number):
    child_details = child_db.find_one({"account_number": account_number})
    if bool(child_details):
        return True, child_details
    else:
        return False, "account dose not exist"


# Verify if account exists
def verify_parent_account(account_number):
    parent_details = parent_db.find_one({"account_number": account_number})
    if bool(parent_details):
        return True, parent_details
    else:
        return False, "account dose not exist"


def transactions_request_child(account_number):
    try:
        child_requests = transaction_request_db.find(
            {"child_account_number": account_number}
        )

        return True, child_requests

    except Exception as e:
        print(e)
        return False, e


def transactions_request_child_from_parent(parent_account_number):
    try:
        child_requests = transaction_request_db.find(
            {"parent_account_number": parent_account_number}
        )

        return True, child_requests

    except Exception as e:
        print(e)
        return False, e


def delete_transaction_request(transaction_request_id):
    try:
        transaction_request_db.delete_one(
            {"transaction_request_id": transaction_request_id})
        return True, "Success"
    except Exception as e:
        print(e)
        return False, e


def transactions_by_child(username, account_number):
    try:
        child_details = child_db.find_one(
            {"username": username, "account_number": account_number})
        child_sent = transaction_db.find(
            {"from_account_number": child_details["account_number"]}
        )

        child_received = transaction_db.find(
            {"to_account_number": child_details["account_number"]}
        )

        return True, child_sent, child_received

    except Exception as e:
        print(e)
        return False, e


def transactions_by_parent(username, account_number):
    try:
        parent_details = parent_db.find_one(
            {"username": username, "account_number": account_number})
        parent_sent = transaction_db.find(
            {"from_account_number": parent_details["account_number"]}
        )

        parent_received = transaction_db.find(
            {"to_account_number": parent_details["account_number"]}
        )

        return True, parent_sent, parent_received

    except Exception as e:
        print(e)
        return False, e


def transactions_by_child_from_parent(parent_account_number):
    try:
        child_details = child_db.find(
            {"parent_account_number": parent_account_number})

        child_sent = []
        child_received = []

        for i in child_details:
            child_transactions_sent = transaction_db.find(
                {"from_account_number": i["account_number"]}
            )

            for j in child_transactions_sent:
                child_sent.append(j)

            child_transactions_received = transaction_db.find(
                {"to_account_number": i["account_number"]}
            )

            for j in child_transactions_received:
                child_received.append(j)

        return True, child_sent, child_received

    except Exception as e:
        print(e)
        return False, e