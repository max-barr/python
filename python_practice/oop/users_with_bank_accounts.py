class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    # instance methods
    def greeting(self):
        print(f"Hello, my name is {self.name}!")
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(f"{self.name}'s account balance is now {self.account_balance} dollars.")
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(f"{self.name}'s account balance is now {self.account_balance} dollars.")
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        print(f"{other_user.name}'s account balance is now {other_user.account.balance} dollars.")
        print(f"{self.name}'s account balance is now {self.account.balance} dollars.")
        return self

class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance=0):
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
        print(f"Balance is currently {self.balance}")
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

# User instances
max = User("Max", "max@gmail.com")
tom = User("Tom", "tommy@yahoo.com")
jimmy = User("Jimmy", "james150@gmail.com")

max.account.deposit(150)
max.display_user_balance()
max.account.display_account_info()
max.transfer_money(tom, 75)
jimmy.account.deposit(500)
jimmy.account.display_account_info()
jimmy.transfer_money(max, 100)

BankAccount.print_all_accounts()