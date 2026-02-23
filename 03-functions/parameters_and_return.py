# parameters and return values

# parameters
# like in the defining functions file...
def hello(name):
    print(f"Hello {name}!")
hello("Alexis")

# multiple parameters
def add(a, b):
    print(a + b)
add(6, 7)

# return values
def multiply(a, b):
    return a * b
result = multiply(6, 7)
print(result)

# difference between print and return
def square(x):
    return x * x
value = square(3)
print(value)

# this function only prints (returns None)
def show_square(x):
    print(x * x)
output = show_square(4)
print(output) # None