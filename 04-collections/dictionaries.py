# Dictionaries
# A dictionary is a collection of key-value pairs. It is also known as a hash map or associative array in other programming languages.
# Key-value pairs, unordered, mutable

person = {
    "name": "Alexis",
    "age": 21
}

# Accessing
print(person["name"])

# Also accessing
print(person.get("age"))

# Adding
person["major"] = "Computer Science"
person["age"] = 22

# Removing
person.pop("age")

# Keys and values
print(person.keys())
print(person.values())
print(person.items())

# Looping
for key in person:
    print(key, person[key])

# Looping key + value
for key, value in person.items():
    print(key, value)