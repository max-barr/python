# Must convert int to string to concatenate 
print("Hello " + str(42))

total = 35
user_value = "25"
# Must convert string to int to add
total = total + int(user_value)
print(total)

# F Strings
first_name = "Jimmy"
last_name = "Chitwood"
age = 19
print(f"Hey, my name is {first_name} {last_name} and I'm {age} years old.")

# String.format()
print("Hey, my name is {} {} and I'm {} years old.".format(first_name, last_name, age))

# % formatting
print("My name is %s %s and I'm %d years old." % (first_name, last_name, age))

# Split string method (default split is every space)
print("Hello World!".split())
print("Hello World!".split("o"))