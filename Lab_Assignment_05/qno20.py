class Bank:
    all_accounts = {}

    @classmethod
    def add_accounts(cls):
        acc = input("Enter the account name = ")
        amount = float(input("Enter the amount = "))
        cls.all_accounts.update({acc : amount})
    
    @classmethod
    def close_accounts(cls):
        close = input("Enter the account to close = ")
        if close not in cls.all_accounts:
            print("No accounts found!!")
        else:
            del cls.all_accounts[close]
            print(f"{close}'s account has been closed.")
    
    @classmethod
    def display(cls):
        for k,v in cls.all_accounts.items():
            print(f"Account Name : {k}, Total Balance : {v}")
    
Bank.add_accounts()
Bank.add_accounts()
Bank.add_accounts()
Bank.display()
Bank.close_accounts()
Bank.display()