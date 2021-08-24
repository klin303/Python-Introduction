# stars.py
# Solution to the stars homework problem

getting_input = True

while getting_input:
    rows = int(input("Please enter the number of rows:")) # ask user for input
    if rows >= 0: # valid input
        getting_input = False
    else:
        print("Input must be positive or zero.")


# when rows = 0
stars = "" # string variable
for i in range(rows):
    stars += "*"
    print(stars)

print("") # spacer line

for i in range(rows):
    stars = "*" * (rows - i)
    spaces = " " * i
    print(spaces + stars)