"""

Author: Ryan Gwin
Date written: 01/17/2025
Assignment:   Module1 Programming Assignment Part1
Short Desc:   take temperature in celsius as user input, convert temp to Fahrenheit, 
            print result to screen


"""

def celsiusToFahrenheit():
    userTemp = input("Enter the temperature in celsius you want converted to Fahrenheit: ")
    conversion  = ((9/5)*float(userTemp))+32
    print(conversion)
    """
        This function takes user's input, degrees celsius and converts it to fahrenheit,
        and prints to screen

    """

celsiusToFahrenheit()