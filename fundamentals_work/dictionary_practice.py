x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x[1])
# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students[0]['last_name'])
# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'][0])
# Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

# ----------------------

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(list):
    # i is now a dictionary
    for i in list:
        # use items method to retrieve keys, values
        for key, val in i.items():
            print(key + ": " + val)

iterateDictionary(students)

# --------------------

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary2(key_name, list):
    # i is now a dictionary
    for i in list:
        print(i[key_name])

iterateDictionary2('last_name', students)

# ------------------

schools = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# print(schools['locations'][1])

def print_info(dict):
    for key in dict:
        print(f"{len(dict[key])} {key}")
        for i in dict[key]:
            print(i)

print_info(schools)
