pets = {}
pets["dog"] = "Dodger"
pets["cat"] = "Buddy"
pets["fish"] = "Captain Smith"
print(pets)
print(pets["fish"])

pets.pop("cat")
print(pets)
pets["dog"] = "Sammy"
print(pets)

thoughts = {
    "questions": [
        {"id": 1, "content": "Why is the sky blue?"},
        {"id": 2, "content": "Why does the wind blow?"},
        {"id": 3, "content": "What is time?"},
        {"id": 4, "content": "What is the meaning of life?"}
    ]
}
print(thoughts["questions"])
print(thoughts["questions"][2])
print(thoughts["questions"][2]["content"])

print(len(thoughts["questions"]))
