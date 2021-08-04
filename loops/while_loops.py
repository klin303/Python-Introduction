# while_loops.py
# Purpose: learn how to use while loops

# Loops in coding are used to execute the same lines of code over and over

# the simplist of these is the while loop

# while (condition):
#     execute

x = 0

while x < 5: # will run until x >= 5
    print(x)
    x += 1 # same as x = x + 1
print("loop completed\n")


y = 0
while y < 0:
    print(y)
    y += 1
print("loop completed\n")


# THIS IS AN INFINITE LOOP, BE CAREFUL
# z = 0
# while z >= 0:
#     print(z)
#     z += 1
# print("loop completed")

# continue and break are loop operators
# you use them inside loops

# break - leaves the loop

y = 1
while y < 10:
    print(y)
    if y == 5:
        break

    y += 1
print("loop completed\n")

# continue - will skip the rest of the loop statement and return to the condition
y = 0
while y < 10:
    y += 1 # y = y + 1
    if y == 5 or y == 6:
        continue
    print(y)
print("loop completed\n")

# error handling with while loops
year = int(input("Enter a year:"))
while year <= 0:
    print("Invalid year")
    year = int(input("Enter a year:"))

print("Year is", year)

# Example: take in a bunch of words one by one and print out the words in a sentence
sentence = ""

while True:
    word = str(input("Enter a word: "))
    if word == "." or word == "!" or word == "?":
        sentence += word
        break
    sentence += " " + word # sentence = sentence + " " + word
    # "hi" + "mom" = "himom"
print(sentence)


