# comparison.py
# Purpose: this program will determine if two user inputted floats are <, >. ==
#          it will also calculate the absolute difference between the two numbers

# retrieve user input
first = float(input("Please enter the first number:"))
second = float(input("Please enter the second number:"))

# determine comparison and calculate absolute difference
if first > second:
    print("Result:", first, "is greater than", second)
    print("The absolute difference is", first - second)
elif first < second:
    print("Result:", first, "is less than", second)
    print("The absolute difference is", second - first)
else:
    print("Result:", first, "is equal to", second)
    print("The absolute difference is", second - first)