num1 = 42 #variable declaration, number
num2 = 2.3 #variable declaration, number
boolean = True #Boolean, variable declaration
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, array, strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, objects, strings, boolean
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, nameError: variable not defined
print(type(fruit)) #log statement
print(pizza_toppings[1]) #log statement, access value
pizza_toppings.append('Mushrooms')
print(person['name']) #log statement, access value
person['name'] = 'George' #change value
person['eye_color'] = 'blue' #change value
print(fruit[2]) #log statement

if num1 > 45:
    print("It's greater") #log statement
else:
    print("It's lower") #conditional, if, else

if len(string) < 5:
    print("It's a short word!") #conditional, if
elif len(string) > 15:
    print("It's a long word!") #else if
else:
    print("Just right!") #else

for x in range(5): 
    print(x)      
for x in range(2,5): 
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5): #while loop
    print(x)
    x += 1

pizza_toppings.pop() #delete value
pizza_toppings.pop(1) 

print(person) #log statement
person.pop('eye_color') #delete value
print(person) #log statement

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #conditional
        continue  #continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #conditional
        break #break

def print_hello_ten_times():
    for num in range(10): #for loop
        print('Hello')

print_hello_ten_times() #log statement

def print_hello_x_times(x):
    for num in range(x): 
        print('Hello')

print_hello_x_times(4) #log statement

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
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
