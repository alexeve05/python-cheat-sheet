# Sets
# A set is an unordered collection of unique elements. It is defined using curly braces {} or the set() constructor.

num = {1, 2, 3, 4}
print(num)

# Adding
num.add(5)

# Removing
num.remove(2)

# Membership
print(3 in num)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# Looping
for n in num:
    print(n)