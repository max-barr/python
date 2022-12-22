class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    # instance methods
    def greeting(self):
        print(f"Hello, my name is {self.name}!")

    def make_deposit(self, amount):
        self.account_balance += amount
        print(f"{self.name}'s account balance is now {self.account_balance} dollars.")

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        print(f"{self.name}'s account balance is now {self.account_balance} dollars.")

    def display_user_balance(self):
        print(f"{self.name}'s account balance is currently {self.account_balance} dollars.")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"{other_user.name}'s account balance is now {other_user.account_balance} dollars.")
        print(f"{self.name}'s account balance is now {self.account_balance} dollars.")

# Create new instance
max = User("Max", "max@yahoo.com")
jimmy = User("Jimmy", "jimmy@hotmail.com")

# Call instance methods
max.greeting()
max.make_deposit(500)
max.transfer_money(jimmy, 300)
