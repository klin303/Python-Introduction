# make_cents.py
# Purpose: Write a program which takes a number as inputs which represent cents
#          The program should calculate the makeup of the coins in quarters, dimes, nickels, and pennies

# Sample I/O
# <<< Enter cents: 86
# <<< 3 Quarters
# <<< 1 Dime
# <<< 0 Nickels
# <<< 1 Penny

# Get user input of cents
cents = int(input("Enter cents:"))

# set coin values in variables
val_quarter, val_dime, val_nickel, val_penny = 25, 10, 5, 1

# Quarters:
#       option 1: looping to try all word
#       option 2: divide - faster
num_quarters = cents // val_quarter # double // is floor division

# calculate remainder for quarters using modulo (%)
cents = cents % val_quarter

# repeat for the remaining coins
# dimes
num_dimes = cents // val_dime
cents = cents % val_dime

# nickels
num_nickels = cents // val_nickel
cents = cents % val_nickel

# pennies
num_pennies = cents // val_penny

# print out the values, adding plural when necessary
if num_quarters > 1 or num_quarters == 0:
    print(num_quarters, "Quarters")
else:
    print(num_quarters, "Quarter")

if num_dimes > 1 or num_dimes == 0:
    print(num_dimes, "Dimes")
else:
    print(num_dimes, "Dime")

if num_nickels > 1 or num_nickels == 0:
    print(num_nickels, "Nickels")
else:
    print(num_nickels, "Nickel")

if num_pennies > 1 or num_pennies == 0:
    print(num_pennies, "Pennies")
else:
    print(num_pennies, "Penny")
