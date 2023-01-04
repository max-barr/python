from pet import Pet

class Person:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    # class methods
    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bathe(self):
        self.pet.noise()
        return self

rocky = Pet("Rocky", "Chihuahua", "jump", 80, 50)
max = Person("Max", "Barr", rocky, "chew", "Kibble")

max.feed().bathe().walk()
print(rocky.health)
print(rocky.energy)