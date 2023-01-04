class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    # Class methods
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += (self.price * percent_change)
        else:
            self.price -= (self.price * percent_change)


