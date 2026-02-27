# Lists
# Ordered collection

# Creating a list
numbers = [1, 2, 3, 4]
mixed = [1, "Hi", True]

# Accessing elements
print(numbers[0])
print(numbers[-1])

# Slicing
print(numbers[1:3])
print(numbers[:2])
print(numbers[2:])

# Modifying
numbers[0] = 10
print(numbers)

# Adding
numbers.append(5)
numbers.insert(1, 99)

# Removing
numbers.remove(99)
numbers.pop()
numbers.pop(0)

# Length
print(len(numbers))

# Looping
for num in numbers:
    print(num)

# Index
for i in range(len(numbers)):
    print(i, numbers[i])