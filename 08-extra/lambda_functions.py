# Lambda Functions
# small anonymous functions

# Regular function
def add(a, b):
    return a + b
print(add(4, 8))

# Lambda version
add_lambda = lambda a, b: a + b
print(add_lambda(3, 7))

# Often used with sorting
numbers = [5, 1, 3, 8]
numbers.sort(key=lambda x: x)
print(numbers)

# Sorting by length
words = ["red", "orange", "purple"]
words.sort(key=lambda word: len(word))
print(words)

# Lambdas should be short and simple