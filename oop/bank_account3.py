class BankAccount:
    all_accounts = []
    # Constructor
    def __init__(self, int_rate = 0.02, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    
    # Class methods
    def deposit(self, amount):
        self.balance += amount
        print(f"Successful deposit of {amount}. Balance is now {self.balance}.")
        return self
    
    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
            print(f"Successful withdrawal of {amount}. Balance is now {self.balance}.")
            return self
        else: 
            self.balance -= 5
            print(f"Insufficient funds. You have been charged a $5 fee. Balance is now {self.balance}.")
    
    def display_account_info(self):
        print(f"Balance is currently {self.balance}.")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            return self
        else:
            print("Cannot yield interest.")
            return self
    
    # CLASS METHOD
    @classmethod
    def display_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()

# Class instances
account1 = BankAccount()
account2 = BankAccount()

account1.deposit(100).deposit(25).deposit(41).withdraw(11).yield_interest().display_account_info()

BankAccount.display_all_accounts()