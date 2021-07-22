# booleanPractice.py
# Purpose: gain practice with comparison.txt operators

# REFERENCE
# and - both items must be true to yield true, else false
# or - only one item must be true to yeild true, else false
# != - does not equal
# == - equals
# <= is less than or equal to, >= is greater than or equal to
# Note: comparisons respect parentheses just like in math

# Instructions : Write down if comparisonResult will yield True or False then
#                run the program to check your answers

x = True
y = False

# Part 1: and/or
comparisonResult = x and y

print(comparisonResult)

comparisonResult = x and x
print(comparisonResult)

comparisonResult = y and y
print(comparisonResult)

comparisonResult = x or y
print(comparisonResult)

comparisonResult = x or x
print(comparisonResult)

comparisonResult = y or y
print(comparisonResult)

print("--- hit Enter for the next set of solutions ---")
input()

# Part 2: equality
x = 10
y = 5

comparisonResult = x == y
print(comparisonResult)

comparisonResult = x != y
print(comparisonResult)

comparisonResult = y == y
print(comparisonResult)

comparisonResult = x != x
print(comparisonResult)

print("--- hit Enter for the next set of solutions ---")
input()

# Part 3: < and >
x = 10
y = 5

comparisonResult = x >= y
print(comparisonResult)

comparisonResult = x <= y
print(comparisonResult)

x = -3
y = -2

comparisonResult = y > x
print(comparisonResult)

comparisonResult = x <= x
print(comparisonResult)

comparisonResult = y < x
print(comparisonResult)

comparisonResult = y >= x
print(comparisonResult)

print("--- hit Enter for the next set of solutions ---")
input()

# Part 4: Combination
x = 10
y = 5
z = 5

comparisonResult = (y >= z) and (x > -1) or (z != y)
print(comparisonResult)

comparisonResult = (x == y) or (x < 0) or (z != x) and (x == 11)
print(comparisonResult)

x = True
y = False

comparisonResult = not (x and y)
print(comparisonResult)