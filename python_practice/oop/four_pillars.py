# Benefits of OOP:
# -- Implements DRY (Don't repeat yourself) principle
# -- Makes application scalable 
# -- Makes code reusable
# -- Makes applications easily maintainable

# 1. ENCAPSULATION
# Encapsulation is the idea that we can group code together into objects; hence Object Oriented Programming. We use classes or "coding blue prints" to define what our objects are and how they behave. We encapsulate attributes and methods in our class.

class CoffeeM:
    def __init__(self, name):
        self.name = name
        self.water_temp = 200
    def brew_now(self, beans):
        print(f"Brewing now using {beans}!")
    def clean(self):
        print("Cleaning")

# -------------------------------------------
# 2. INHERITANCE
# Inheritance is the idea that we pass along attributes and methods from one class into a "sub-class" or child class, and not have to re-write the code to make it work.  Child classes can be more specific versions of their Parent class.  Using the key word "super" will call methods.

