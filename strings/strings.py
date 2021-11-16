# introduction to string iteration

string = "hello"
separated_string = ""

# enhanced for loops
for character in string:
    # separated_string += character + ' '
    print(character)
"h e l l o "
print(separated_string)
# ASCII - pairs characters to numbers

code = "sdfhsk7j7j7sdjsd"
is_7 = False # boolean to track if there is a 7
for c in code:
    if c == '7':
        is_7 = True # set is_7 to true if we find a 7

if is_7:
    print("There is a 7!")
else:
    print("There is no 7")