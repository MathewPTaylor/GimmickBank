# Bank code stuff


class FileFuncs:
    @staticmethod
    def ReadFile(filename: str):
        with open(filename, "r") as f:
            return f.read().splitlines()

    @staticmethod
    def AppendtoFile(filename: str, content: str):
        with open(filename, "a") as f:
            f.write(content + "\n")

class Bank:
    def __init__(self):
        self.db = []

    def loadBankDetails(self):
        # get bank details of every user
        user_details = FileFuncs.ReadFile("Bank_details.txt")

        # splitting each user info string into a list with proper data types
        for i in range(len(user_details)):
            # splitting the string into a list
            user_details[i] = user_details[i].split()
            
            # making the user balance a float
            user_details[i][-1] = float(user_details[i][-1])

        self.db = user_details
            
            
            
    def addUser(self, username: str, password: str):
        FileFuncs.AppendtoFile("Bank_details.txt", f"{username} {password} 0")

    def update_user




BankObj = Bank()

BankObj.add_user("Test124", "Test124")

BankObj.load_bank_details()

print(BankObj.db)

input()
