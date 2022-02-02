################################################################################
# Lists Introduction Homework
################################################################################

################################################################################
# Tasks:
# 1. Fill in the code to get the length of a list 
# 2. Fill in the code to check if a number is in a list
# 3. Fill in the code to return the index of a list element
################################################################################


################################################################################
# Task 1
################################################################################
# This function will return the length of the list, arr
def get_length(arr):
    ### WRITE CODE HERE ###
    pass # remove when done


################################################################################
# Task 2
################################################################################
# This function will return True if x is in arr
# or False if x is not in the arr
def is_element(arr, x):
    ### WRITE CODE HERE ###
    pass # remove when done


################################################################################
# Task 3
################################################################################
# This function will return the index of element x or -1 if x is not in arr
def get_index(arr, x):
    ### WRITE CODE HERE ###
    pass # remove when done





















################################################################################
################################################################################
# TESTING CODE - DO NOT EDIT BELOW
################################################################################
################################################################################
# test arrays
arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = ['hi', 'bye', 'dog', 'cat', 'blue', 'red']
arr3 = []



def test_function(function_name, test, expected):
    if test == expected:
        print("Test Passed")
    else:
        print(function_name, "failed a test case.")


# length
test_function('get_length', get_length(arr1), 11)
test_function('get_length', get_length(arr2), 6)
test_function('get_length', get_length(arr3), 0)

# is_element
test_function('is_element', is_element(arr1, 10), True)
test_function('is_element', is_element(arr2, 'dog'), True)
test_function('is_element', is_element(arr3, 10), False)

# get_index
test_function('get_index', get_index(arr1, 7), 9)
test_function('get_index', get_index(arr1, 11), -1)
test_function('get_index', get_index(arr2, 'bye'), 1)
test_function('get_index', get_index(arr3, 1), -1)
