class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.bank_name = "Bank of the West"
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"Hi, {self.name}. Your balance is {self.account_balance}.")
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

Max = User("Max Williams", "max@gmail.com")
Richard = User("Richard Brinkly", "richardb@yahoo.com")

Max.make_deposit(150).make_deposit(22).transfer_money(Richard, 22).display_user_balance()
Richard.display_user_balance()

