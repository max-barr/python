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

# NESTED DICTIONARIES

# List of dictionaries
users = [
    {"first": "Ada", "last": "Lovelace"}, # index 0
    {"first": "Alan", "last": "Turing"}, # index 1
    {"first": "Eric", "last": "Idle"} # index 2
]
# Dictionary of lists
resume_data = {
    #        	     0           1           2
    "skills": ["front-end", "back-end", "database"],
    #                0           1
    "languages": ["Python", "JavaScript"],
    #                0              1
    "hobbies":["rock climbing", "knitting"]
}

print(users[0]["last"])
print(resume_data["skills"][1])
print(users[2]["first"])