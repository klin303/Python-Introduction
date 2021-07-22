# Purpose: take two integers as input and output the sum

# Gets user input
print("Please enter the first number:")
firstNum = input()
print("Please enter the second number:")
secNum = input()

# casts the input as integers
# casting is representing one data type as another
firstNum = int(firstNum)
secNum = int(secNum)

# calculate the sum
sum = firstNum + secNum
diff = firstNum - secNum

print("The sum is:", sum)
print("The difference is:", diff)

