# lets write a program to get someone's first name 

fullName = input("Enter a full name: ")

for i, letter in enumerate(fullName):
    if letter == ' ':
        print(fullName[ : i])
        print(fullName[i + 1: ])

