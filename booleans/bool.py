# a boolean is a variable type that is either True or False
# booleans are really good for comparing things

correct = True
print("Correct is", correct)

wrong = False
print("Wrong is", wrong)

# the way we get boolean values besides setting them to True and False is comparison.txt operators
# Some ones you know already are : < and >

x = 10 < 20 # x is a boolean
print("10 < 20 is", x)

x = 10 > 20 # x is a boolean
print("10 > 20 is", x)

x = 10 <= 20 # less than or equal to
print("10 < 20 is", x)

x = 10 >= 20 # greater than or equal to
print("10 > 20 is", x)

# Equality Operators
x = 10 == 10 # in programming, comparison.txt equals is represted with ==
print("10 == 10 is", x)

x = 10 == 20
print("10 == 20 is", x)

x = 10 != 10 # NOT in programming is represented with an exclamation point
print("10 != 10 is", x)

x = 10 != 20
print("10 != 20 is", x)

x = True
x = not x
print("The opposite of True is", x)

x = not x
print("The opposite of the opposite of True is", x)

# And and Or
# For an and comparison.txt to be true, both parts must be true, else it will be false
# True and True = True
# True and False = False
# False and False = False

x = True
y = False

result = x and y # result will be false
print("x and y is", result)

# an OR statement will be true if one or more of the parts true
# True or True = True
# True or False = True
# False or False = False

result = x or y # result will be false
print("x or y is", result)

result = (5 < 10) and (10 != 10)
# will reduce to True and False
# so final answer will be False

result = not(10 == 10) or (35 >= 35)
# reduces to not True or True
# reduces to False or True
# Final answer is True

result = (10 != 5) or (11 < 11) or (not False) and (0 >= 1)
# reduces to True or False or True and False
# reduces to True          or True and False
# reduces to True                  and False --> want to move from left to right
# final answer is False