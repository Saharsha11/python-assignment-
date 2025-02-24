class Account:
    
    def __init__(self,cust_no,acc_no,acc_type,balance):
        self.cust_no = cust_no
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = balance
    
class SavingAccount(Account):

    def deposit(self):
        amount = int(input("Enter the amount to deposit = "))
        self.balance += amount
        print(f"Rs {amount} has been deposited.")

    def display(self):
        print(f"Total balance of the account = {self.balance}")

    def withdraw(self):
        amount = int(input("Enter the amount to withdraw = "))
        self.balance -= amount
        print(f"Rs {amount} withdrawn")
        print(f"Total balance = {self.balance}")
    
s = SavingAccount(5860,111254478,"Saving Accounts",750000)
s.deposit()
s.display()
s.withdraw()