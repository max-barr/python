class BankAccount:
    accounts = []
    def __init__(self, name, int_rate, balance=0):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    # Class methods
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. Balance is now {self.balance}.")
        return self
    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrawal successful. Balance is now {self.balance}.")
        return self
    def display_account_info(self):
        print(f"{self.name} balance is currently {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print("Insufficient funds.")
        return self
    
    # Class method
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

# Child class
class RetirementAccount(BankAccount):
    def __init__(self, name, int_rate, is_roth, balance=0):
        super().__init__(name, int_rate, balance)
        self.is_roth = is_roth

checking = BankAccount("Checking", 0.01)
savings = BankAccount("Savings", 0.02)

checking.deposit(200).deposit(150).deposit(300).withdraw(100).yield_interest().display_account_info()
savings.deposit(1000).deposit(2000).withdraw(150).withdraw(200).withdraw(150).withdraw(300).yield_interest().display_account_info()

BankAccount.print_all_accounts()
