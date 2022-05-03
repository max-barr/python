class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.bank_name = "Bank of the West"
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"Hi, {self.name}. Your balance is {self.account_balance}.")
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

Max = User("Max Williams", "max@gmail.com")
Richard = User("Richard Brinkly", "richardb@yahoo.com")

Max.make_deposit(150)
Max.make_deposit(22)
Max.transfer_money(Richard, 22)
Max.display_user_balance()
Richard.display_user_balance()

