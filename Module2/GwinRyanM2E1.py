"""
Author: Ryan Gwin
Date Written: 01/26/2025
Assignment: Module2 Programming Assignment Part 1

Insructions:
get 2 primary colors from user,
if one or both of the colors are not primary colors, put out error message
mix the 2 primary colors and put out the correct secondary color

"""
#create lists of primary and secondary colors
primaryColors = ['red', 'blue', 'yellow']
secondaryColors = ['purple', 'green', 'orange']

#add input for 2 primary colors
primary1 = input('Please input a primary color (red, blue, yellow): ').lower()
primary2 = input('Please enter another primary color (red, blue, yellow): ').lower()


#restrict user input to correct values
while (primary1 not in primaryColors) or (primary2 not in primaryColors):
    primary1 = input('Error: one of your colors was not a primary color. Please input a primary color (red, blue, yellow): ').lower()
    primary2 = input('Please enter another primary color (red, blue, yellow): ').lower()

#mix red and blue
if (((primary1 == primaryColors[0]) or (primary1 == primaryColors[1])) and ((primary2 == primaryColors[0]) or (primary2 == primaryColors[1]))):
    print(f"{primary1} and {primary2} make {secondaryColors[0]}.".capitalize())

#mix blue and yellow
if (((primary1 == primaryColors[1]) or (primary1 == primaryColors[2])) and ((primary2 == primaryColors[1]) or (primary2 == primaryColors[2]))):
    print(f"{primary1} and {primary2} make {secondaryColors[1]}.".capitalize())
#mix red and yellow
if (((primary1 == primaryColors[0]) or (primary1 == primaryColors[2])) and ((primary2 == primaryColors[0]) or (primary2 == primaryColors[2]))):
    print(f"{primary1} and {primary2} make {secondaryColors[2]}.".capitalize())


