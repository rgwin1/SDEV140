"""
Author: Ryan Gwin
Date Written: 01/21/2025
Assignment: Module2 Practice Exercise 3-9

Insructions: Write a program in a file named sum.py that receives a series of numbers from the user and allows the user to press the enter key to indicate they are finished providing inputs. After the user presses the enter key, the program should print the sum of the numbers and their average.

"""

#create while loop to take constant input until a certain value is input.

#define variables
print("This is a summation calculator.  Every number you enter will be added to the last one.")
theSum = 0
count = 0
print("Please enter the first number to be added or press Enter to finish: ")
#get the starting input from user
userInput = input("Enter a number or press Enter to quit: ")

#start loop, adding each number gotten from user to the previous number gotten from user until Enter (an empty string) is hit
while userInput != '': #conditional for loop to check
    while (userInput.isdigit() == False) and (userInput != ''): #checks to make sure user input is an int
        userInput = input("You have entered an invalid value. Please, enter a number or press Enter to quit: ") 
    theSum += float(userInput) #converts user input to int type for simple addition
    count += 1 #determines dividend for final average
    print(theSum) #to show user accruing sum
    userInput = input("Enter a number or press Enter to quit: ")
    if userInput == '': #checks for exit
        print(f"The sum is {theSum}.")
        if count > 0: 
            print(f"The average is {theSum/count}")
        else:
            print("No count available")


    
