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



john = User("John", "Johnson", "john@yahoo.com", 34)
john.display_info().enroll().display_info().spend_points(150).display_info()