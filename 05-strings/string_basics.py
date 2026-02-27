# Strings
# A string is a sequence of characters. In Python, strings are enclosed in either single quotes (' ') or double quotes (" ").

text = "hello"

# Indexing
print(text[0])
print(text[-1])

# Slicing
print(text[1:4])
print(text[:3])
print(text[3:])
print(text[::2])

# Length
print(len(text))

# Looping through a string
for char in text:
    print(char)

# Strings are immutable
# create a new string
text = "H" + text[1:]
print(text)