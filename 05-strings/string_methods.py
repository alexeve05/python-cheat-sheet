# Common String Methods

text = " Hello world "

# case methods
print(text.lower())
print(text.upper())
print(text.title())

# Removing space
print(text.strip())
print(text.lstrip())
print(text.rstrip())

# Replacing
print(text.replace("world", "mars"))

# Splitting
sentence = "red, green, blue"
print(sentence.split(","))

# Joining
words = ["Hello", "world"]
print(" ".join(words))

# Checking content
print("Hello".startswith("He"))
print("Hello".endswith("o"))
print("123".isdigit())
print("abc".isalpha())
print("abc123".isalnum())


# Finding
print("Hello".find("1"))

# tip: string methods do not modify the original string, they return a new string.

text = "hello"
new_text = text.upper()
print(text)
print(new_text)