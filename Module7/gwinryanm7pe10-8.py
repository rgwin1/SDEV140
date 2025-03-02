"""
Module for playing cards, with classes Card and Deck

Assignment: Practice Exercise 10-8
Date Written: 03/01/2025
Author: Ryan Gwin

Description:  Create a Card class with rank and suit attributes, including a faceup attribute that determines if the card is face up or down.

Create a Deck class as a collection of 52 Card objects, with methods for shuffling and dealing cards.

Instantiate a deck, shuffle it, and deal cards while displaying their information to the screen.
""" 
import random

class Card(object):
    """ A card object with a suit and rank."""

    RANKS = tuple(range(1, 14))

    SUITS = ("Spades", "Diamonds", "Hearts", "Clubs")

    def __init__(self, rank, suit):
        #initializes a card with a rank and suit
        self.rank = rank
        self.suit = suit
        self.faceup = False  #new instance variable
    
    def turn(self):
        #toggles the faceup attribute
        self.faceup = not self.faceup
        
    def __str__(self):
        #returns the string representation of a card
        if self.rank == 1:
            rank = "Ace"
        elif self.rank == 11:
            rank = "Jack"
        elif self.rank == 12:
            rank = "Queen"
        elif self.rank == 13:
            rank = "King"
        else:
            rank = self.rank
        return str(rank) + " of " + self.suit

import random

class Deck(object):
    """ A deck containing 52 cards."""

    def __init__(self):
        #creates a full deck of 52 cards
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                c = Card(rank, suit)
                self.cards.append(c)

    def shuffle(self):
        #shuffles the deck
        random.shuffle(self.cards)

    def deal(self):
        #removes and returns the top card, or None if empty
        if len(self) == 0:
            return None
        else:
            return self.cards.pop(0)

    def __len__(self):
        #returns the number of remaining cards in the deck
        return len(self.cards)

    def __str__(self): 
        #returns the string representation of the deck
        result = ''
        for c in self.cards:
            result = self.result + str(c) + '\n'
        return result

def main():
    #a simple test for the deck
    deck = Deck()
    print("A new deck:")
    while len(deck) > 0:
        print(deck.deal())
    deck = Deck()
    deck.shuffle()
    print("A deck shuffled once:")
    while len(deck) > 0:
        print(deck.deal())

if __name__ == "__main__":
    #runs the main function if script is executed
    main()
