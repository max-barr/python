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
        for product in self.products:
            product.update_price(percent_increase, True)
        return self
    def set_clearance(self, category, percent_discount):
        pass 
    def print_products(self):
        for product in self.products:
            # print(f"{product.name}, {product.category}, {product.price}")
            product.print_info()


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def update_price(self, percent_change, is_increased):
        change_amount = self.price * percent_change
        if is_increased == True:
            self.price += change_amount
        else:
            self.price -= change_amount
        return self
    def print_info(self):
        print(f"{self.name}, {self.category}, {self.price}")


safeway = Store("Safeway")

bread = Product("bread", 2.99, "baked goods")
milk = Product("milk", 1.99, "dairy")
peanut_butter = Product("peanut butter", 3.50, "pantry items")


safeway.add_product(bread).add_product(milk).add_product(peanut_butter).print_products()

safeway.inflation(0.02).print_products()

safeway.sell_product(1).print_products()


# bread.print_info()