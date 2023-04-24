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

    def on_sale(self, percent_off):
        self.price *= (1 - percent_off)

    def add_tax(self, tax):
        self.price *= (1 + tax)

    def price_cut(self, money):
        if money > self.price:
            print("Sorry, we can't cut the price of this shoe.")
            return False
        else: 
            self.price -= money

    def hike_price(self, money):
        self.price += money

# Instances
dress_shoe = Shoe("Cole Haan", "Work Shoe", "Dress", 89.99, True)
bball_shoe = Shoe("Nike", "KD 15", "Basketball", 150, False)


bball_shoe.add_tax(.07)
bball_shoe.price_cut(30)
bball_shoe.hike_price(60)
bball_shoe.on_sale(0.2)
print(bball_shoe.price)

dress_shoe.stock_check()
bball_shoe.stock_check()



