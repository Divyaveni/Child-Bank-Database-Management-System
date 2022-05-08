import os
from datetime import datetime
from random import randint

import bcrypt
from dotenv import load_dotenv
from pymongo import MongoClient, DESCENDING, ASCENDING

load_dotenv()
client = MongoClient(os.getenv("MONGODB"))
db = client.cbdbms
parent_db = db.parent
child_db = db.child


def parent_signup(name, username, password, phone, email):
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    parent_db.create_index(
        [("username", DESCENDING), ("email", DESCENDING), ("phone", ASCENDING), ("account_number", ASCENDING)],
        unique=True)
    parent_details = {
        "name": name,
        "username": username,
        "email": email,
        "password": hashed_password,
        "phone": phone,
        "balance": 0,
        "account_number": randint(1000000000, 10000000000),
        "createdAt": datetime.now()
    }
    try:
        parent_db.insert_one(parent_details)
        return True
    except Exception as e:
        print(e)
        return False


def child_signup(name, username, password, parent_account_number, dob, email):
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    child_db.create_index([("username", DESCENDING), ("account_number", ASCENDING)], unique=True)
    parent_details = {
        "name": name,
        "username": username,
        "email": email,
        "password": hashed_password,
        "parent_account_number": int(parent_account_number),
        "account_number": randint(1000000000, 10000000000),
        "createdAt": datetime.now(),
        "balance": 0,
        "dob": dob
    }
    try:
        child_db.insert_one(parent_details)
        return True
    except Exception as e:
        print(e)
        return False