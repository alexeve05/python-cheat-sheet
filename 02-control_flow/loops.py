# Loops
# used to repeat code

# while loop
count = 0
while count < 5:
    print(count)
    count += 1 # IMPORTANT: update variable to avoid infinite loop

# for loop (with range())
for i in range(5):
    print(i) # range(stop)
for i in range(1, 6):
    print(i) # range(start, stop)
for i in range(0, 10, 2):
    print(i) #range*(start, stop, step)

# looping through list
colors = ["purple", "blue", "green"]
for color in colors:
    print(color)

# break and continue
for i in range(10):
    if i == 5:
        break # stop loop completely
    print(i)
for i in range(5):
    if i == 2:
        continue # skip this specific iteration
    print(i)

# nested loops
for i in range(3):
    for j in range(2):
        print(i, j)

# WARNING
# if you forget to update the loop variable, you may create an infinite loop.