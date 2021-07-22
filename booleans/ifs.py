# ifs.py
# Purpose: Review if, if/else, and else if statements

grade = input("Please enter a number grade:")
grade = float(grade) # casting grade to a float

# next, we want to check that the grade is valid (0 <= grade <= 100)

# whatever is in parantheses is true or false
if(grade >= 0 and grade <= 100):
    print("This grade is valid.")
else:
    print("This grade is NOT valid.")
    print("try again")

print("Moving on to grading...")

# now we want to determine if the student passed
if(grade >= 60):
    print("You passed!")
else:
    print("You failed :(")

# now lets assign a letter
letter = '' # we declare letter here so we can use it later

# else if statements will only perform one true if
if(grade >= 90):
    letter = 'A' # letter is only in the scope of this if, if I declare it here
elif(grade >= 80): # this is an else if statement
    letter = 'B'
elif(grade >= 70):
    letter = 'C'
elif(grade >= 60):
    letter = 'D'
else:
    letter = 'F'

if(letter == 'F'):
    if(grade + 1 >= 60):
        letter = 'D'
        print("You passed with extra credit")
    else:
        print("Unfortunately, you have to do summer school")
else:
    print("Good job passing!")


print("Letter grade: ", letter)

