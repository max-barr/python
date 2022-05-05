class BankAccount:
    accounts = []
    def __init__(self, int_rate = 0.02, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
        else: 
            print("Insufficient Funds: Charging $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

Checking = BankAccount()
Savings = BankAccount()

Savings.deposit(100).deposit(120).deposit(140).withdraw(70).yield_interest().display_account_info()
Checking.deposit(75.46).deposit(89.90).withdraw(7.99).withdraw(6).withdraw(59.99).withdraw(3.99).yield_interest().display_account_info()

BankAccount.print_all_accounts()
