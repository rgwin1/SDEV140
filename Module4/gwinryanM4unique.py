"""
Author: Ryan Gwin
Date Written: 02/06/2025
Description:

Create a program to access text file, read the file, adding text as a string.
Split the string into words
remove punctuation and duplicate words,
sort list
print out to screen
"""

#get user input for text file
fileName = input('Enter the file name you want to open: ')
inputFile = open(fileName, 'r')
text = inputFile.read()
inputFile.close()

#split words and add them into an array
allWords = text.split()
uniqueWords = []
#iterate over array --eliminating duplicate words, stripping punctuation, and making everything lowercase
for word in allWords:
    if '.' in word:
        word = word.strip('.').lower()
    elif ',' in word:
        word = word.strip(',').lower()

    if word not in uniqueWords:
        uniqueWords.append(word.lower())

#alphabetize list
uniqueWords.sort()

for word in uniqueWords:
    print(word)


        