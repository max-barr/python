person = {
    "first": "Max",
    "last" : "Barr",
    "age" : 38,
    "is_organ_donor": True
}

person["email"] = "max@hotmail.com"
print(person)

if "email" not in person:
    print("That email is not in use")
    person["email"] = "jimmy@gmail.com"
else:
    print("Email already in use")

print(person["email"])
print("My name is " + person["first"] + " " + person["last"])

value_removed = person.pop("is_organ_donor")
print(person)