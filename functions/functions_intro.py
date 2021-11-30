"""
Functions

What are functions?
    - Functions are simply commands in your code which will perform a task

What do functions do?
    - Sometimes the functions will physically give you something back
    - Sometimes the function will change what you give it

Why do we use functions?
    - They're very useful! They can take care of a lot of boring, tedious tasks that we would otherwise have to do
    - They help us organize our programs into different sections which all perform a specific tasks
    - They allow us to reduce how much code we write. Instead of writing the same few lines of code 10 times, we could
      just write 1 function.

How do you use functions?
    - When we use functions, we have to call them in the code
    - This normally involves just writing the function name with parentheses ()
"""

"""
What are some examples of functions? 
    - We have actually already used some functions in our code
    - The input() function is designed to give you (return) whatever the user types in "string" form
    - The int("12") function will take a string or char and convert it into an int -> 12
    - And of course we have print() which we use all the time!
"""

# get user input
user_input = input()
print(user_input)

# convert a string into an integer
txt = "12"
number = int(txt)
print(number + 1)

"""
How to identify functions?
    - You can normally tell what things are functions by the parentheses after their name
    - Ex: int(), input()
    
Why do some functions require things inside the parentheses and others don't?
    - Sometimes, functions require information to perform their tasks. For example, the int() function needs to know
      what we want to convert to an int
    - In order for the functions to work, we need to pass in information. The information we pass in are called 
      parameters.
    - Some functions take no parameters, some take many. It all depends on what the function is designed to do
    - Sometimes, the parameters are optional
"""

# The input function has an optional parameter
# We can use input without parameters like this...
user_input = input()
print(user_input)

# We can also give input a parameter, in this case it's a prompt we want to print before the user enters something
user_input = input("Please enter something: ")
print(user_input)

"""
Here is a new function which is very very very useful. It's called the len() function, short for length

What it does?
    - Returns to you how long something is ... it can be used on many many things
    - For now, we will just talk about how to use it with strings
        - Calling len("txt") with a string as the parameter will return to you how many characters are in the string
"""

txt = "word"
# calling len(txt) will give you 4 since there are 4 characters in "word"
length = len(txt)
print(length)

# here is another example
txt = "count me!"
txt_length = len(txt)
print(txt_length)

# here is an example where you can enter something
user_input = input("Enter something:")
length_input = len(user_input)
print("Length of the string you entered:", length_input)

"""
Sometimes, functions belong to / are a part of bigger collections. For example, strings have many functions which 
belong to them. 

When using these functions, we have to call them using the . symbol
For string functions, we would to string.function()

A good one to look at first is the lower() function

string.lower()
    - What does it do? -> converts a string to all lowercase letters
    - Does it take parameters? -> nope
    - How do we use it? -> string.lower()
        - string would be the string we want to convert to lowercase
"""

string = "HELLO"
lower_string = string.lower()
print(lower_string)

# here is another exmaple, what do you think happens to the lower-case letters
txt = "Hi Mom!"
print(txt.lower())
# here we say that txt is calling the lower function
# txt in a way owns the lower function and is telling it to do something like how you might tell your microwave to run

"""
Here is another, slightly more complicated function
string.count("target")
    - What does it do? -> counts how many times the target string appears in the string calling the function
    - Does it take parameters? -> yes! the target string we are looking for
    - How do we use it? -> txt.count(target)
        - txt would be the string we want to look in
        - target would be the string we are looking for
"""

search_string = "go google"
target_string = "go"
target_count = search_string.count(target_string) # go should appear 2 times in the search string
print(target_count)

search_string = "substitute subway sub"
target_string = "sub"
#######################
# You try printing out how many times the target appears
#######################

# CODE HERE



"""
A good function for our calculator project will be the isdigit() function. 

string.isdigit()
    - What does it do? -> returns True (boolean) if the string is made up of just numbers
                       -> returns False (boolean) if the string id not made up of just numbers
    - Parameters? -> None
"""

sample1 = "1234456"
# Write code to check if sample1 is just numbers

# CODE HERE


sample2 = "123_not_a_number"
# repeat for sample 2

# CODE HERE

sample3 = "123.5"
# and again, the result might suprise you

# CODE HERE





############################################################################################################
# This is a function I wrote for the calculator project, you can copy and paste it into your code
# It will check if a number is a float or not
# It works much like isdigit() but with support for floats

def is_float(txt):
    try:
        float(txt)
        return True
    except ValueError:
        return False

