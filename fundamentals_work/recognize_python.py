num1 = 42 #variable declaration, numbers
num2 = 2.3 #variable declaration, numbers
boolean = True #variable declaration, boolean
string = 'Hello World' #variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, list of strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, dictionary of key:valiue pairs, strings, numbers, boolean
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, tuple
print(type(fruit)) #type check, tuple
print(pizza_toppings[1]) #list, access value of index 1
pizza_toppings.append('Mushrooms') #list, add value, String
print(person['name']) #Dictionary, access value
person['name'] = 'George' #Dictionary, change value, String
person['eye_color'] = 'blue' #Dictionary, add value, String
print(fruit[2]) #Tuple, access value, String

#Conditional, if else statment
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

#Conditional, if, else if, else statement
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# For loop range is 0-4
for x in range(5): 
    print(x)

# For loop range is 2-4
for x in range(2,5):
    print(x)

#For loop range is 2-9, increment by 3
for x in range(2,10,3):
    print(x)

# While loop
x = 0
while(x < 5):
    print(x)
    x += 1

# Remove final value in list
pizza_toppings.pop()

#Remove index 1 from list
pizza_toppings.pop(1)

# Access full dictionary
print(person) 
#Remove eye color from dictionary
person.pop('eye_color')
print(person)

# For loop, continue, break
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

# Function with for loop, prints Hello 10 times (range 0-9)
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

# Function call
print_hello_ten_times()

# Function with argument x, for loop. Prints Hello x times
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

# Function call
print_hello_x_times(4)

# Function with argument x, default value of 10, for loop.
# If no argument given, will print 10 times
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print("--Between functions--")
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)