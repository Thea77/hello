people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Daro", "house": "BBB"},
    {"name": "Draco", "house": "CCC"},
]

# def f(person):
#     return person["name"]

# lamda expression
people.sort(key=lambda person: person["name"])

print(people)