# mod.py
# learn about modulo

# in programming, modulo or "mod" is an arithmetic operator
# mod is used to return the remainder of division
# it is identified using the '%' symbol

# 5 % 2 = 1
# 10 % 4 = 2
# 99 % 3 = 0
# 4 % 5 = 4
# 0 % 10 = 0

# mod, like division, can't be done by 0
# you CAN'T do 10 % 0

num = int(input("Enter a number:"))

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")
