local_val = "father"

def square(x):
    return x * x

class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"

print(square(4))
user = User("Emma")
print(user.name)
print(user.say_hello())