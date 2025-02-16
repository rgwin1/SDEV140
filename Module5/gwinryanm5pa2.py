"""
Author: Ryan Gwin
Date Written: 02/16/2025

Description: Guessing game.  Computer generates a random number between 1 and 100.
User guesses number. If number too low, or too high, user guesses again.  User guesses,
until correct number guesed. User gets to play again if user chooses.


"""



import random

def guessing_game():
    """
    generates a random number between 1 and 100 and prompts the user to guess it.
    provides feedback on whether the guess is too high or too low and restarts upon correct guess.
    """
    number=random.randint(1, 100)
    while True:
        try:
            guess=int(input("Guess a number between 1 and 100: "))
            if guess<number:
                print("Too low, try again.")
            elif guess>number:
                print("Too high, try again.")
            else:
                print("Congratulations! You guessed the correct number.")
                number=random.randint(1, 100)  #restart the game with a new number
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")

#start the game
guessing_game()
