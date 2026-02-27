# Reading and Writing Files

# Opening a file
# Modes:
# "r" - read (default)
# "w" - write (overwrites file)
# "a" - append
# "r+" - read and write

# Reading
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Writing
with open("example.txt", "w") as file:
    file.write("hello\n")
    file.write("world\n")

# Appending
with open("example.txt", "a") as file:
    file.write("new line\n")

# read()
with open("example.txt", "r") as file:
    print(file.readline())
    print(file.readlines())

# Use "with", it automatically closes the file for you
# Avoid:
file = open("example.txt", "r")
content = file.read()
file.close()