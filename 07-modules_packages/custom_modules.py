# Creating Custom Modules
# Suppose we create another file called math_utils.py

# math_utils.py
# ---------------------
# def add(a, b):
#     return a + b
#
# def multiply(a, b):
#     return a * b

# Importing our module
import math_utils
print(math_utils.add(2, 3))
print(math_utils.multiply(4, 5))

# Importing specific functions
from math_utils import add
print(add(10, 5))

# Main guard
# This code runs only if the file is executed directly

if __name__ == "__main__":
    print("This file is being run directly")