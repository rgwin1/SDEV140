"""
Author: Ryan Gwin
Date Written: 01/26/2025
Assignment: Module2 Programming Assignment Part 1

Insructions:
write a program that allows a user to enter a nonnegative integer, then uses a loop to calculate the factorial of that number. Display the factorial.

"""

#take user input, should be a positive integer
factorial = input("Enter a nonnegative whole number: ")
check = factorial.isdigit() 
if (check == True):
    factorial = int(factorial)
else: 
    while ((check == False) or (int(factorial) <= 0)): #comparison should check to make sure factorial is an integer value, and greater than 0
        factorial = input("You either didn't enter a number or your number was less than or equal to 0. Please enter a whole number greater than 0: ")
        check = factorial.isdigit()
        if (check == True):
            factorial = int(factorial)
#create value for iteration to multiply on to
total = 1

#iterate until factorial is complete
for num in range(1, factorial + 1):
    total *= num
    
print(f"{factorial}! is {total}.")