# Logical Operators
# used to combine conditions

# and -> True if BOTH conditions are True
print(True and True)   # True
print(True and False)  # False

# or -> True if AT LEAST ONE condition is True
print(True or False)   # True

# not -> reverses the boolean value
print(not True)  # False

# EXAMPLES with variables
age = 20
hasID = True

if age >= 18 and hasID:
    print("You may enter.")

# combining multiple comparisons
x = 7
if x > 5 and x < 10:
    print("x is between 5 and 10")

# cleaner way
if 5 < x < 10:
    print("x is between 5 and 10")