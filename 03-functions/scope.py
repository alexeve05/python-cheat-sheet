# scope
# determines where a variable can be accessed

# local
def my_function():
    x = 10
    print(x)
my_function()
# print(x) : error (x does not exist outside function)

# global
y = 20
def print():
    print(y)
print()

# modifying global (not recommended but yk...)
count = 0
def increase():
    global count
    count += 1
increase()
print(count)

# TIP: Avoid using global variables when possible, pass values as parameters instead