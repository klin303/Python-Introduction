# for_loops
# Purpose: learn how to use for loops

# Basic for loop
# for loops are best used for doing something a specific amount of times
# when making a for loop, you declare a variable to keep track of the count
# the common convention is to use i (followed by j, k, etc... if you are nesting the loop)

# range(x) - this means from 0 to x (x not included)
for i in range(3): # i will be increased by 1 each time the loop runs
                   # so the loop runs 3 times
    print(i)

# range(x, y) - this means from x to y (x inclusive, y exclusive)
#               starting from x ending at y
for i in range(10, 15):
    print(i)

 # we can also nest the for loops
for i in range(5):
    string = ""
    for j in range(10):
        string += "+"
    print(string)
