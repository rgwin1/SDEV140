"""
Author: Ryan Gwin
Date Written: 02/01/2025

Instructions: 
Write a program that writes a series of random numbers to a file and displays all the numbers to the console. Each random number should be in the range of 1 through 500. The application should let the user specify how many random numbers the file will hold. (15 points)

"""
#used for random value generation
import random


#get user input to determine how many numbers will be written to the file and printed to the console
totalNums = input("Please enter the total number of random integers you want to write to the file: ")

#validation check
while totalNums.isdigit() == False:
    totalNums = input("Please enter the total number of random integers you want to write to the file: ")

totalNums = int(totalNums)
#generate array of random numbers. 
randomNumbers = [random.randint(0, 500) for randomNumber in range(1, totalNums + 1)]
# print(randomNumbers)
with open("randomNumbers.txt", "w") as file:
    for number in randomNumbers:
        if (number == randomNumbers[-1]):
            file.write(str(number))
        else:
            file.write(str(number) + ', ')
file.close()
print(randomNumbers)

