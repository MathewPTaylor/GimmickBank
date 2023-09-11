# Bank code stuff
from DBFuncs import *

class Bank:
    def __init__(self):
        self.userInfo = {}

    def addUser(self, username, password, dbobj):
        dbobj.addRecord(username, password, 0.0)

    def loadUserInfo(self, dbobj):
        self.userInfo = dbobj.FetchAllRecords()

    




Db = DBFuncs("Users.db")

Db.addField("USERNAME", "text", True)
Db.addField("PASSWORD", "text")
Db.addField("BALANCE", "real")



BankObj = Bank()
