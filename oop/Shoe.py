class Shoe:
    def __init__(self, brand, name, activity, price, in_stock):
        self.brand = brand
        self.name = name
        self.activity = activity
        self.price = price
        self.in_stock = in_stock
    
    # METHODS
    def stock_check(self):
        if self.in_stock == True:
            print(f"Yes, the {self.brand} {self.name} is in stock")
        else: 
            print(f"Sorry, the {self.brand} {self.name} is currently out of stock")



dress_shoe = Shoe("Cole Haan", "Work Shoe", "Dress", 89.99, True)
bball_shoe = Shoe("Nike", "KD 15", "Basketball", 150, False)

dress_shoe.stock_check()
bball_shoe.stock_check()



