# Exception Handling

# Basic try / except
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except:
    print("Something went wrong.")

# Catching
try:
    x =int(input("Enter a number: "))
    print(10 / x)
except ValueError:
    print("Invalid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Else block
try: 
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid number.")
else:
    print("You entered: ", x)

# Finally block
try:
    file = open("example.txt", "r")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Done.")

# Raising exceptions
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# Avoid catching all exceptions blindly
# except SpecificError: