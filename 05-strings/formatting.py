# String formatting

name = "Alexis"
age = 21
gpa = 3.924

# Concatentation
print("Hello " + name)

# must convert numbers into strings
print("Age: " + str(age))

# f-strings
print(f"Hello {name}")
print(f"Next year you will be {age +1}")

# Formatting numbers
print(f"Gpa: {gpa:.2f}")

# Format method
print("Hello {}".format(name))
print("Age: {}".format(age))

# Multiple placeholders
print("{} is {} years old.".format(name, age))

# Multi line strings
message = f"""
Name: {name}
Age: {age}
"""
print(message)