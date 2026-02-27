# Common Patterns with Collections
# These are patterns frequently used in beginner programming problems.

# Counting with a dictionary
words = ["red", "orange", "red", "blue", "orange", "red"]
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)

# Cleaner version using .get()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)

# Finding the maximum in a list
numbers = [21, 39, 27, 9, 56]
max_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num
print(max_value)

# Built-in version
print(max(numbers))

# Finding the minimum in a list
min_value = numbers[0]
for num in numbers:
    if num < min_value:
        min_value = num
print(min_value)

# Built-in version
print(min(numbers))

# Summing values in a list
total = 0
for num in numbers:
    total += num
print(total)

# Built-in version
print(sum(numbers))

# Searching for an item
target = 7
found = False
for num in numbers:
    if num == target:
        found = True
        break
print(found)

# Cleaner version
print(target in numbers)

# bUilding a new list / filtering
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(evens)

# Looping through dictionaires

student_grade = {
    "Alexis" : 90,
    "Brittany": 85,
    "Chris": 95
}
for name, grade in student_grade.items():
    print(name, grade)

# Nested collections
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for value in row:
        print(value)