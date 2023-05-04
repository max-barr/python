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

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = BankAccount()

    # METHODS
    def display_info(self):
        print(f"{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\nRewards member: {self.is_rewards_member}\nGold Card Points: {self.gold_card_points}")
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print("User is already a member")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return self

    def spend_points(self, amount):
        if self.gold_card_points - amount > 0:
            self.gold_card_points -= amount
            print(f"{self.first_name} {self.last_name} has successfully spent {amount} gold card points.")
            return self
        else:
            print(f"{self.first_name} {self.last_name} does not have enough points.")
            return self
        
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info()
        return self

# Class instances
account1 = BankAccount()
account2 = BankAccount()

account1.deposit(100).deposit(25).deposit(41).withdraw(11).yield_interest().display_account_info()

BankAccount.display_all_accounts()

john = User("John", "Johnson", "john@yahoo.com", 34)
john.make_deposit(200)
john.display_user_balance()