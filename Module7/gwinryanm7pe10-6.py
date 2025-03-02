"""
Module for simulating a dice-based game using the Player class.

Assignment: Practice Exercise 10-8
Date Written: 03/01/2025
Author: Ryan Gwin

Description:  Create a Player class that manages rolling two dice, tracking game state variables, and determining win/loss conditions.

Define functions to play a single game interactively and multiple games with statistical tracking.

Instantiate a Player object, roll dice, and display game results based on player interactions.
"""
from die import Die

class Player(object):

    def __init__(self):
        """Has a pair of dice and initializes game state variables."""
        self.die1 = Die()
        self.die2 = Die()
        self.roll = ""
        self.rollsCount = 0
        self.atStartup = True
        self.winner = False
        self.loser = False
        self.point = None
    
    def __str__(self):
        """Returns the string representation of the most recent roll."""
        return self.roll

    def rollDice(self):
        """Rolls the dice once, updates state, and returns the roll values."""
        self.die1.roll()
        self.die2.roll()
        v1, v2 = self.die1.getValue(), self.die2.getValue()
        self.roll = f"({v1}, {v2}) {v1 + v2}"
        self.rollsCount += 1
        rollSum = v1 + v2
        #logic for the first roll
        if self.atStartup:
            if rollSum in (7, 11):
                self.winner = True
            elif rollSum in (2, 3, 12):
                self.loser = True
        #logic for the following rolls       
            else:
                self.point = rollSum
                self.atStartup = False
        else:
            if rollSum == 7:
                self.loser = True
            elif rollSum == self.point:
                self.winner = True
        
        return v1, v2
    
    def getNumberOfRolls(self):
        """Returns the number of rolls made."""
        return self.rollsCount
    
    def isWinner(self):
        """Returns True if the player has won."""
        return self.winner
    
    def isLoser(self):
        """Returns True if the player has lost."""
        return self.loser

#defined outside of the player class
def playOneGame():
    """Plays a single game interactively."""
    player = Player()
    while not player.isWinner() and not player.isLoser():
        #continue rolling until player wins or loses
        input("Press Enter to roll the dice...")
        v1, v2 = player.rollDice()
        print(player.roll)
    if player.isWinner():
        print("You win!")
    else:
        print("You lose!")

def playManyGames(number):
    """Plays multiple games and prints statistics."""
    wins = 0
    losses = 0
    totalRolls = 0
    #play through the specified number of games
    for count in range(number):
        player = Player()
        while not player.isWinner() and not player.isLoser():
            player.rollDice()
        totalRolls += player.getNumberOfRolls()
        if player.isWinner():
            wins += 1
        else:
            losses += 1
    print("Total Wins:", wins)
    print("Total Losses:", losses)
    print("Average Rolls per Game:", totalRolls / number)

def main():
    """Runs the main game loop."""
    #player chooses number of games to play
    choice = input("Play a single game (1) or multiple games (2)? ")
    if choice == "1":
        playOneGame()
    else:
        number = int(input("Enter the number of games to play: "))
        playManyGames(number)


if __name__ == "__main__":
    main()
