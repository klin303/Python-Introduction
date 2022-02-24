# arr = ['a', 'b', 'c', 'd']

# for x in arr:
#     print(x)


import enum
from turtle import pos


homeroom = ['Jack', 'Ben', 'Sally', 'Megan']

# for student in homeroom:
#     if student == 'Ben':
#         print(student, 'was late!')


# for i in range(len(homeroom)):
#     if homeroom[i] == 'Ben':
#         print(homeroom[i], 'was late!')




finishing_order = ['Jack', 'Ben', 'Sally', 'Megan']
# there is something with enhanced loops called enumerate
# enumerate allows us to get the index of what we are traversing

for i, racer in enumerate(finishing_order):
    print(i)
    print(racer) 




finishing_order = ['Jack', 'Ben', 'Sally', 'Megan']
# define a function to determine the position where someone ordered
# parameters:
#   order is a list of the finishing order
#   target is the name of the racer we are searching for

# name of the function: position
def position (order, target):
    for i, person in enumerate(order):
        if person == target:
            return i + 1

result = position(finishing_order, 'Sally')
print()
print()
print('Sally', result)
print('Ben finished', position(finishing_order, 'Ben'))



race_2 = ['Sally', 'Ben', 'Jack', 'Megan', 'Rob']
print(position(race_2, 'Sally'))

# scan the finishing order
# when we find target - calculate her finishing position