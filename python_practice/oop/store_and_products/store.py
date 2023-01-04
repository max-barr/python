class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
    # Class methods
    def add_product(self, new_product):
        self.products.append(new_product)
        print(f"{new_product} has been added to the store.")
        return self