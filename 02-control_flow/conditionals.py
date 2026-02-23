# Conditionals
# used to run code only if a condition is True

x = 10

#basic if statement
if x > 5:
    print("x is greater than 5")

# if / else
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# if / elif / else
grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("F")

# nested conditionals
age = 20
isStudent = True
if age >= 18:
    if isStudent:
        print("Adult student")
    else:
        print("Adult")

# important
# indentation matters in Python
# use 4 spaces (recommended)

# this will cause an error:
# if x > 5:
# print("x is greater than 5")