# Importing Modules
# a module is a python file containing code (functions, variables, etc)

# Importing a module
import math
print(math.sqrt(81))
print(math.pi)

# Importing specific functions
from math import sqrt, pi
print(sqrt(16))
print(pi)

# Import with alias
import math as m
print(m.sqrt(25))

# Import everything
from math import *
print(sqrt(9))

# Common modules
import random
print(random.randint(1, 10))

import datetime
print(datetime.date.today())

# Python searches for modules in the current folder, installed packages, and puthons standard library.