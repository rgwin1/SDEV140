"""
author: Ryan Gwin
Date Written: 02/22/2025
description: The program guesses a number, and the user provides feedback until it’s correct. 
It narrows the range based on user input until the guess is inevitable correct.  Allows user to
start a new game.
"""

from breezypythongui import EasyFrame
import random

class App(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        #low is the lower boundary that gets reset, high is the upper boundary that gets reset
        self.low = 1
        self.high = 100
        self.random_num = random.randint(self.low, self.high)
        self.current_num = self.random_num
        self.label = self.addLabel(text = f"Is the number {self.current_num}?", row = 0, column = 0, columnspan = 4, sticky='N')
        self.label.columnconfigure(0, weight = 1)

        #create buttons
        self.too_small_button = self.addButton(text = "Too Small",row = 1, column = 0, command = self.too_small)
        self.too_large_button = self.addButton(text = "Too Large",row = 1, column = 1, command = self.too_large)
        self.correct_button = self.addButton(text = "Correct",row = 1, column = 2, command = self.correct_number)
        self.new_game_button = self.addButton(text = "New Game",row = 1, column = 3, state="disabled", command = self.new_game)

    def too_small(self):
        """ tell computer that number is too_small, reassign lower end, and get new random int above lower end"""
        self.low = self.current_num + 1
        if self.low >= self.high:
            self.too_small_button["state"] = "disabled"
            self.too_large_button["state"] = "disabled"
        self.current_num = random.randint(self.low, self.high)
        self.label["text"] = f"Is the number {self.current_num}?"

    def too_large(self):
        """tell computer that number is too large, reassign upper end, get new random int below upper end"""
        self.high = self.current_num - 1
        if self.low >= self.high:
            self.too_small_button["state"] = "disabled"
            self.too_large_button["state"] = "disabled"
 
        self.current_num = random.randint(self.low, self.high)
        self.label["text"] = f"Is the number {self.current_num}?"
        
    def correct_number(self):
        """tell computer number guessed is correct, disable 3 other buttons, enable new_game button"""
        self.too_small_button["state"] = "disabled"
        self.too_large_button["state"] = "disabled"
        self.correct_button["state"] = "disabled"
        self.new_game_button["state"] = "normal"

    def new_game(self):
        """starts a new game"""
        self.low = 1
        self.high = 100
        self.random_num = random.randint(self.low, self.high)
        self.current_num = self.random_num
        self.label["text"] = f"Is the number {self.current_num}?"
        self.too_small_button["state"] = "normal"
        self.too_large_button["state"] = "normal"
        self.correct_button["state"] = "normal"
        self.new_game_button["state"] = "disabled"
        
def main():
    App().mainloop()


if __name__ == "__main__":
    main()




