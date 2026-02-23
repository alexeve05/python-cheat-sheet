# Functions
# a reusable block of code

# basic function
def hello():
    print("Hello!")

# calling (running) a function
hello()

# why use functions?
# functions with parameters
def say_hello(name):
    print(f"Hello, {name}!")
    print("Welcome to Python.")

say_hello("Alexis")
say_hello("Matt") # reuse without rewriting code

# IMPORTANT 
# defining a function does not run it.
# you must call the function.