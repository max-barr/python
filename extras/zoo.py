class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
    
    def display_info(self):
        print(f"Name: {self.name}, Health: {self.health}, Happiness: {self.happiness}")
        return self

    def feed(self):
        self.health += 10
        self.happiness += 10
        return self
    
class Lion( Animal ):
    def __init__(self, name, age, hunger, health = 75, happiness = 55):
        super().__init__(name, age, health, happiness)
        self.hunger = hunger
    
    def feed(self):
        self.health += 15
        self.happiness += 15
        self.hunger -= 30
        print("ROAR!")
        return self
    
    def display_info(self):
        print(f"Name: {self.name}, Health: {self.health}, Happiness: {self.happiness}, Hunger: {self.hunger}")
    

class PolarBear( Animal ):
    def __init__(self, name, age, warmth, health = 50, happiness = 25):
        super().__init__(name, age, health, happiness)
        self.warmth = warmth

    def feed(self):
        self.health += 25
        self.happiness += 25
        self.warmth += 15
        print("Need more fish!")
        return self

    def display_info(self):
        print(f"Name: {self.name}, Health: {self.health}, Happiness: {self.happiness}, Warmth: {self.warmth}")

class Otter( Animal ):
    def __init__(self, name, age, warmth, health = 60, happiness = 75):
        super().__init__(name, age, health, happiness)
        self.warmth = warmth

    def feed(self):
        self.health += 5
        self.happiness += 5
        self.warmth += 5
        print("Time for a swim!")
        return self

    def display_info(self):
        print(f"Name: {self.name}, Health: {self.health}, Happiness: {self.happiness}, Warmth: {self.warmth}")

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
    
    def add_lion(self, name, age, hunger):
        self.animals.append( Lion(name, age, hunger) )
        print("Lion added to zoo")
        return self
    
    def add_polar_bear(self, name, age, warmth):
        self.animals.append( PolarBear(name, age, warmth) )
        print("Polar bear added to zoo")
        return self

    def add_otter(self, name, age, warmth):
        self.animals.append( Otter(name, age, warmth) )
        print("Otter added to zoo")
        return self

    def display_zoo_info(self):
        print("-"*30, self.zoo_name, "-"*30)
        for animal in self.animals:
            animal.display_info()

simba = Lion("Simba", 13, 80)
simba.feed().display_info()

peter = PolarBear("Peter", 5, 70)
peter.feed().display_info()

otto = Otter("Otto", 2, 65)
otto.feed().feed().display_info()

zoo1 = Zoo("My Zoo")
zoo1.add_lion("Simba", 13, 80).add_polar_bear("Peter", 5, 70).add_otter("Otto", 2, 65).display_zoo_info()
