"""
Author: Ryan Gwin
Date Written: 02/08/2025
Description:
Takes a user input as an integer, 
checks each number up to the user number to see if each number is a prime,
if not a prime, does not store it. If a prime, stores it in a list.
Prints the list of primes.

"""



#define function for checking primes
def is_prime(n):
    """Check if a number is prime."""
    for i in range(2, n):  
        if n % i == 0:
            return False  
    return True  

#get user input for an integer value
num = input("Enter an integer greater than 1: ")
if (num.isdigit() == True):
    num = int(num)
else:
    while ((num.isdigit() == True) and (int(num) <= 1) or (num.isdigit() == False)):
        num = input("Please enter an integer value greater than 1: ")
    num = int(num)

# Create a list of numbers from 2 up to the user-entered number (inclusive)
numList = list(range(2, num + 1))

#print the prime numbers up to the user number
print("Prime numbers:")
for number in numList:
    if is_prime(number):
        print(number, end=" ")
