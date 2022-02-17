arr = ['apple', 'banana', 'cherry', 'date', 'eggplant']

len(arr) = 5
index of 'cherry'? 2
index of 'eggplant'? 4

arr[0] = 'apple'
arr[4] = 'eggplant'
arr[len(arr) - 1] = 'eggplant'

len(arr) - 3 = 2
arr[2] = 'cherry'

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

len(nums) = 9
nums[3] = 4

(nums[0]) + (nums[3]) = 5
1          +  4        = 5

nums[2] + nums[7] = 11

nums[len(nums) - 1] - nums[6] = 1
nums[0] * nums[1] * nums[2] = 6


letters = [a, b, c, d, e, f, g]

len(letters) = 7

for i in range(len(letters)):
    print(letters[i])



i = 0   --> letters[i] --> a 
i = 1   --> letters[i] --> b
i = 2   


tens = [10, 20, 30, 40, 50, 60, 70, 80, 90]

for i in range(8): 
    print(tens[i + 1])



for i in range(len(tens)):
    if tens[i] < 40:
        print(i)


def add(x, y):
    sum = x + y 
    return sum


def average(x, y):
    avg = (x + y) / 2
    return avg


z = add(1, 2) + add(3, 4)

v = average(5, 10)