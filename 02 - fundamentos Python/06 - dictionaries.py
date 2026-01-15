
user = {
    "name": "Gael",
    "age": 21,
    "email": "gael@gmail.com",
    "is_active": True,
    "skills": ["Python", "JavaScript", "C++"],
    (25.686327, -100.316870): "Nuevo León"
}

user["name"] = "Gael Alguiar"
user["country"] = "Mexico"
print(user)
print(user[(25.686327, -100.316870)])

# Values, items, keys
print(user.values())
print(user.items())
print(user.keys())

