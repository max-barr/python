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

# Create new instance
max = User("Max", "max@yahoo.com")

# Call instance methods
max.greeting()
max.make_deposit(500)
