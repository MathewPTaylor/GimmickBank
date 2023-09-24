# Bank code stuff
from DBFuncs import *
import sys

class Bank:
    actions = [
        "Deposit",
        "Withdraw",
        "Check balance"
        ]
    def __init__(self):
        self.userInfo = {}
        self.db = DBFuncs("Users.db")
        
    def addUser(self, username: str, password: str, balance: float = 0.0):
        # adding the new user to the database
        self.db.addRecord(username, password, balance)

        # adding the new user to self.userInfo for right away use of the account
        self.userInfo[username] = {
            "USERNAME": username,
            "PASSWORD": password,
            "BALANCE": balance
            }
        
    def loadAllUserInfo(self):
        self.userInfo = self.__convertFetchedDatatoDict(self.db.FetchAllRecords())

    def __convertFetchedDatatoDict(self, fetcheddata) -> dict:
        # each key will be the username
        thedict = {}
        for user in fetcheddata:
            thedict[user[0]] = {
                "USERNAME": user[0],
                "PASSWORD": user[1],
                "BALANCE": user[2]
                }
            
        return thedict

    def checkUsernameAvailabilty(self, username):
        return not username in self.userInfo.keys()

    def VerifyUser(self, username, password):
        if username in self.userInfo.keys():
            if password == self.userInfo[username]["PASSWORD"]:
                return True
        return False
        # SHORTER VERSION (harder to understand): return username in self.userInfo.keys() and password == self.userInfo[username]["PASSWORD"]


# Initialising bank object and the db object

BankObj = Bank()

BankObj.db.tableName = "USERS"

BankObj.db.addField("USERNAME", "text", True)
BankObj.db.addField("PASSWORD", "text")
BankObj.db.addField("BALANCE", "real")

BankObj.loadAllUserInfo()

def inputUntilDesiredValue(*desiredinputvals, inputmessage="", errormessage=""):
    while True:
        inputVal = input(inputmessage)
        if inputVal in desiredinputvals:
            return inputVal
        else:
            print("Invalid input", file=sys.stderr)

def ActionsLoop():
    print("What would you like to do?:")
    for num, action in enumerate(Bank.actions):
        print(f"{num+1}. {action}")

    action = input(">")

class Validation:
    @staticmethod
    def ValidateUsername(username):
        return not len(username) < 5

    @staticmethod
    def ValidatePassword(password):
        if len(password) < 5:
            return False
        hasnum = False
        for let in password:
            if let in "1234567890":
                hasnum = True
        if not hasnum:
            return False
        
        return True
    
# START OF THE UI
def Mainloop():
    print(BankObj.userInfo)
    hasAccount: bool = False

    print("-----MOTHER'S BANK-----")

    # asking the user if they have an account already or not
    hasAccountInput = inputUntilDesiredValue("yes", "no", inputmessage="Do you have an account with us? (yes, no): ", errormessage="Invalid Input.")
    
    # turning the user input into a True or False
    hasAccount = {"yes":True,"no":False}[hasAccountInput]

    if hasAccount: # the user has an account
        # login
        username = input("Username: ")
        password = input("Password: ")
        if not BankObj.VerifyUser(username, password):
            print("Account does not exist.", file=sys.stderr)
            return
        
        # display possible actions (deposit, withdraw, check balance, loan)
        ActionsLoop()
        
    else: # the user does not have an account
        # display sign up stuff
        # check if the username is unique or not
        while True:
            username = input("Username: ")
            if BankObj.checkUsernameAvailabilty(username):
                break
            else:
                print("Username already exists.", file=sys.stderr)
                
        password = input("Password: ")
        #inputUntilDesiredValue()
        while True:
            confirmPassword = input("Confirm password: ")
            if confirmPassword == password:
                break
            else:
                print("Password and confirm have different values.", file=sys.stderr)
                
        # adding the new user to the db
        BankObj.addUser(username, password)
        
        print("Account successfully made.")



Mainloop()



