"""
Author: Ryan Gwin
Date Written: 02/08/2025
Description:  This code reads a file, stores its contents as a string, splits it into a sorted word list, 
and creates a dictionary mapping each word to its frequency. 
It then updates the word counts and prints the results in alphabetical order.

"""

#get user input for file and open the file in read mode
fileName = input("Enter the name of the file: ")
inputFile= open(fileName, 'r')

#save file text as a string and close file
text = inputFile.read()
inputFile.close()

#split file text into a list and alphabetize
listText = text.split()
listText.sort()

#create dictionary
concordance = dict.fromkeys(listText, 0)

#iterate over list and update values in dictionary
for word in listText:
    concordance[word] = concordance.get(word, 0) + 1

#iterate over dictionary and print results to screen
for key, value in concordance.items():
    print(key, value)



