class Person:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bathe(self):
        self.pet.noise()
        return self

class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    def play(self):
        self.health += 5
        return self
    def noise(self):
        print("Woof! Woof!")
        return self

Fido = Pet("Fido", "Yellow Lab", ["Running", "Jumping", "Playing Fetch"], 75, 55)
James = Person("James", "Williams", Fido, "Chicken Hearts", "Healthy Choice")

James.walk().feed().bathe()

print(f"Health: {Fido.health}")
print(f"Energy: {Fido.energy}")