# List Comprehension
# compact way to create lists

numbers = [1, 2, 3, 4]
squares = []
for n in numbers:
    squares.append(n * n)
print(squares)

# list comp ver
squares = [n * n for n in numbers]
print(squares)

# With condition
evens = [n for n in numbers if n % 2 == 0]
print(evens)

# Transforming strings
words = ["red", "blue"]
uppercase = [word.upper() for word in words]
print(uppercase)