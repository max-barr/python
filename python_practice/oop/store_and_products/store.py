from product import Product

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
    # Class methods
    def add_product(self, new_product):
        self.products.append(new_product)
        print(f"{new_product.name} has been added to the store.")
        return self
    def sell_product(self, id):
        self.products.pop(id)
        print(self.products)
        return self
    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
        return self
    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
        return self

# Store instance
qfc = Store("QFC")

# Products instances
peanut_butter = Product("Peanut Butter", 3.99, "Pantry Food")
milk = Product("Milk", 4.79, "Dairy")
sliced_turkey = Product("Sliced Turkey", 5, "Deli Meats")
sliced_ham = Product("Sliced Ham", 6, "Deli Meats")

qfc.add_product(peanut_butter).add_product(milk).add_product(sliced_ham).add_product(sliced_turkey)

qfc.sell_product(1)

# qfc.inflation(0.3)
qfc.set_clearance("Deli Meats", 0.30)

for product in qfc.products:
    product.print_info()