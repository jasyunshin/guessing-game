# Name: Jason Shin
# Period: AM
# Assignment: Number Guessing Game

# Uses the random module to choose a secret number.
import random

random_number = random.randint(1, 10)
previous_guesses = []
correct_answer_picked = False
tries_remaining = 5

print("Welcome to the Number Guessing Game!")
print("Guess a whole number between 1 and 10.")
print("You have 5 tries!")

# Keeps the game running until the player wins or runs out of tries.
while correct_answer_picked == False and tries_remaining > 0:
    user_guess = int(input("Enter a number between 1 and 10: "))

    # Rejects numbers outside the range and repeated guesses.
    while user_guess < 1 or user_guess > 10 or user_guess in previous_guesses:
        if user_guess < 1 or user_guess > 10:
            print("Invalid input! Enter a number between 1 and 10.")
        else:
            print("You already guessed that number! Choose another.")
            print("Previous guesses:", previous_guesses)

        user_guess = int(input("Enter a number between 1 and 10: "))

    previous_guesses.append(user_guess)

    # Checks the guess and subtracts a try only when it is incorrect.
    if user_guess == random_number:
        correct_answer_picked = True
        print("You guessed correctly! The number was", random_number)
        print("Your guesses:", previous_guesses)
    elif user_guess > random_number:
        print("The random number is lower!")
        tries_remaining = tries_remaining - 1
        print("Previous guesses:", previous_guesses)
        print("Tries remaining:", tries_remaining)
    else:
        print("The random number is higher!")
        tries_remaining = tries_remaining - 1
        print("Previous guesses:", previous_guesses)
        print("Tries remaining:", tries_remaining)

# Reveals the answer if the player loses.
if correct_answer_picked == False:
    print("You ran out of tries!")
    print("Your guesses:", previous_guesses)
    print("The correct number was", random_number)
    print("Game over!")