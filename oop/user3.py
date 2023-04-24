class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    # METHODS
    def display_info(self):
        print(f"{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\nRewards member: {self.is_rewards_member}\nGold Card Points: {self.gold_card_points}")



john = User("John", "Johnson", "john@yahoo.com", 34)
john.display_info()