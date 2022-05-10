class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
    
    def add_product(self, new_product):
        self.products.append(new_product)
        return self

    def sell_product(self, id):
        for product in range(id, len(self.products) - 1):
            temp = self.products[product]
            self.products[product] = self.products[product + 1]
            self.products[product + 1] = temp
        self.products.pop()
        return self

    def inflation(self, percent_increase):
        for product in range(0, len(self.products -1)):
            product.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for product in range(0, len(self.products -1)):
            if product.category == category:
                product.price -= (product.price * percent_discount)
        return self

    def print_products(self):
        for product in self.products:
            product.print_info()

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += (self.price * percent_change)
        else:
            self.price -= (self.price * percent_change)
        return self
    
    def print_info(self):
        print(f"Product: {self.name}, Category: {self.category}, Price: {self.price}")

qfc = Store("QFC")

peanut_butter = Product("Peanut Butter", 4, "Food")
sliced_turkey = Product("Sliced Turkey", 7.99, "Food")
bread = Product("Bread", 3.99, "Food")

qfc.add_product(peanut_butter).add_product(sliced_turkey).add_product(bread).print_products()