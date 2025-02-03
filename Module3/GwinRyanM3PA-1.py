"""
Author: Ryan Gwin
Date Written: 02/01/2025
Assignment: Module3 Programming Assignment Part 1

Insructions:
get number as user input, must be more than one digit.
take each digit from string and add to a total count.
display count.

non-integer input will display error and request userinput again.
"""

#get user input, a number with more than 1 digit:
userNum = input('Please enter a number with more than 1 digit (e.g 12, 123, 1234, etc): ')

#user input validation check.  Make sure user input is an integer value
while userNum.isdigit() == False:
    userNum = input('You entered a value that is not an integer. Please enter a number with more than one digit: ')


#get length
lenUserNum = len(userNum)

#get max index
maxIndex = (len(userNum)-1)

#loop through and add each index value to numCount
index = 0
numCount = 0
while index <= maxIndex:
    numCount += int(userNum[index])
    index += 1


#print total value
print(numCount)

