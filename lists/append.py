# adding to a list is called appending 
arr  = [1]

# len(arr)
# print(arr)

# Lists have their own set of built-in functions 
# append( *what you want to append* ) 
# List.append(x) -> adds x to the end of the list

arr.append(2)

# print(arr)
arr.append('a')
print(arr) 

arr.append([3, 4])
print(arr) 
print(arr[3])

def add_end(arr, x):
  arr.append(x)

list_1 = [1, 2]
print(list_1)

add_end(list_1, 'h')
print(list_1)

# makes a list that holds numbers 0 through n, not including n 
def make_range(n):
  arr = []
  for i in range(n):
    arr.append(i)
  return arr 

range_5 = make_range(5) # [0, 1, 2, 3, 4]
print(range_5)

print(make_range(9))




# returns a list with all the even numbers between 0 and (n - 1)
# get_evens(5) -> [2, 4] 
# get_evens(6) -> [2, 4]
# get_evens(2) -> []
def get_evens(n):
  

