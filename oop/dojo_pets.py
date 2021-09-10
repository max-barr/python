class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    def walk(self):
        self.pet.play()
    def feed(self):
        self.pet.eat()
    def bathe(self):
        self.pet.noise()

class Pet:
    def __init__(self, type, tricks):
        self.health = 80
        self.energy = 60
        self.type = type
        self.tricks = tricks
    def sleep(self):
        self.energy += 25
    def eat(self):
        self.energy += 5
        self.health += 10
    def play(self):
        self.health += 5
    def noise(self):
        print("Ruff! Ruff!")


rocky = Pet("chihuahua", "sit")
max = Ninja("Max", "Barr", "carrots", "kibble", rocky)

# max walks rocky
max.walk()

# max feeds rocky
max.feed()

# max bathes rocky
max.bathe()

print(rocky.health)
print(rocky.energy)