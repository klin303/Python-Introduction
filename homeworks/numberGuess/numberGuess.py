# numberGuess.py
# Purpose: Play a number guessing game!
#
# How to Play:
#     1. The program generates a random number between 1 and 30
#     2. The user will input a guess
#     3. The program will tell the user if the guess is too high or too low
#     4. The program will keep doing this until the user guesses the number
#     5. After the user guesses the number, the program will output the number of attempts it took


# Sample I/O
#
# <<< Welcome to the number guesser!
# <<< The computer has generated a random integer between 1 and 30. Start guessing!
# >>> Please enter a guess: 10
# <<< Too low! Try again...
# >>> Please enter a guess: 20
# <<< Too high! Try again...
# >>> Please enter a guess: 17
# <<< Correct!
# <<< That took 3 attempts.


########################################################
### STARTER CODE, DO NOT EDIT
########################################################

from random import randrange

# generate a random value between 1 and 30 (inclusive)
random_num = randrange(1, 31)

# print instructions
print("Welcome to the number guesser!")
print("The computer has generated a random integer between 1 and 30. Start guessing!")

# WRITE CODE HERE

guess = int(input("Enter number: "))
attempts = 1

while guess != random_num:
    if guess < random_num:
        print("Too low! Try again...")
    elif guess > random_num:
        print("Too high! Try again...")
    guess = int(input("Enter number: "))
    attempts = attempts + 1

print("Correct!")
print("That took", attempts, "attempts.")


