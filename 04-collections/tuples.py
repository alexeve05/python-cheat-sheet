# Tuples
# A tuple is an immutable sequence of values. Tuples are similar to lists, but they cannot be modified after they are created. They are defined using parentheses () instead of square brackets [].

point = (3, 6)

# Access
print(point[0])

# Tuples cannot be changed
# point[0] = 10 ERROR

# Unpacking
x, y = point
print(x)
print(y)

# Single element tuple
single = (5, )