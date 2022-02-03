# python lists
# created using the []

empty_array = [] # empty list


array = ['a', 'b', 'c', 'd']

# each item in the list is called an 'element'
# length of this list = # of elements

# indexes = position of the elements, starting at 0 in python
first_element = array[0]
last_element = array[3]

# list properities
# list length - get it using the 'len' function
list_length = len(array)
# print(list_length)

empty_length = len(empty_array)
# print(empty_length)

# traversing of list
grades = [99, 98, 100, 78, 45, 82, 100]
num_grades = len(grades)

# using a regular for loop
# for i in range(num_grades):
#     print(grades[i])


# i   | grades[i]
# -----------------
# 0   |  99
# 1   |  98
# 2   |  100
# 3   |  78
# ....
# 6   |  100


num_100s = 0
for i in range(num_grades):
    # every time we reach an element == 100, we count 1 one-hundred
    if grades[i] == 100:
        num_100s += 1

# print("Total 100's:", num_100s)

# function
def average(array):
    num_elems = len(array)
    total_sum = 0
    for i in range(len(array)):
        total_sum += array[i]
    return total_sum / num_elems

print(average(grades))
    
    

