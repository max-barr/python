class Pet:
    def __init__(self, name, species, tricks, health, energy):
        self.name = name
        self.species = species
        self.tricks = tricks
        self.health = health
        self.energy = energy
    # class methods
    def sleep(self):
        self.energy += 25
        print(f"{self.name} is sleeping.")
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} is eating.")
        return self
    def play(self):
        self.health += 5
        print(f"{self.name} is playing!")
        return self
    def noise(self):
        print("WOOF!")
        return self

