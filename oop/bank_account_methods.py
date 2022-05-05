class BankAccount:
    # class attribute
    bank_name = "Bank of the East"
    all_accounts = []
    
    # constructor
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    
    # class method to change bank name
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
    
    # class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum
    
    # class method to withdraw funds
    @classmethod
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self

    # statci method to determine if user can withdraw
    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True