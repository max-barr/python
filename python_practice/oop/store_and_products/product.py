class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    # Class methods
    def update_price(self, percent_change, is_increased):
        change_amount = self.price * percent_change
        if is_increased == True:
            self.price += change_amount
        else:
            self.price -= change_amount
        return self
    def print_info(self):
        print(f"Name: {self.name}\nCategory: {self.category}\nPrice: {self.price}")
        return self


