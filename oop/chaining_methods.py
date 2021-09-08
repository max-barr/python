class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"{self.name}, Balance: {self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance +=amount
        print(f"{self.name}, Balance: {self.account_balance}")
        print(f"{other_user.name}, Balance: {other_user.account_balance}")
        return self



max = User("Max Barr", "max@hotmail.com")
rocky = User("Rocky Balboa", "rocky@hotmail.com")
jack = User("Jack Reacher", "jackreacher@aol.com")

max.make_deposit(500).make_deposit(500).make_deposit(500).make_withdrawal(250).display_user_balance()
# max.make_deposit(500)
# max.make_deposit(500)
# max.make_deposit(500)
# max.make_withdrawal(250)
# max.display_user_balance()

rocky.make_deposit(50).make_deposit(150).make_withdrawal(175).make_withdrawal(10).display_user_balance()
# rocky.make_deposit(50)
# rocky.make_deposit(150)
# rocky.make_withdrawal(175)
# rocky.make_withdrawal(10)
# rocky.display_user_balance()

jack.make_deposit(10000).make_withdrawal(250).make_withdrawal(250).make_withdrawal(250).display_user_balance()
# jack.make_deposit(10000)
# jack.make_withdrawal(250)
# jack.make_withdrawal(250)
# jack.make_withdrawal(250)
# jack.display_user_balance()

max.transfer_money(jack, 200)