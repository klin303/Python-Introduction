# leapYear.py
# Purpose: checks if an inputted year is a leap year

# get input from user
year = int(input())

# first check if year is divisible by 4
# if not, we immediately know it is not a leap year
if year % 4 == 0:
    # if it is divisible by 4, we must then check for century years
    # if it is not a century year, we know immediately it is a leap year
    if year % 100 == 0:
        # checking if the year is divisible by 400
        if year % 400 == 0:
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")