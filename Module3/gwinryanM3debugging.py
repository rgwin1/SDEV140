"""
Author: Ryan Gwin
Computes and displays the Flesch Index and the Grade
Level Equivalent for the readability of a text file.

Description: Find the bug that causes the miscount of 
syllables causing the Flesch index to be inaccurate.

Date Written: 01/29/2025
"""

# Take the inputs
fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
text = inputFile.read()
inputFile.close()

# Count the sentences
sentences = text.count('.') + text.count('?') + \
            text.count(':') + text.count(';') + \
            text.count('!')

# Count the words
words = len(text.split())

# Count the syllables
syllables = 0
vowels = "aeiouAEIOU"
for word in text.split():
    for vowel in vowels:
        syllables += word.count(vowel)
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            syllables -= 1
    if word.endswith('le'):
        syllables += 1
    
    # Handle consecutive vowels 
    index = 0
    while index < len(word) - 1:
        if word[index] in vowels and word[index + 1] in vowels:
            syllables -= 1  # Don't count the second vowel
        index += 1

# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / sentences) - \
        84.6 * (syllables / words)
level = int(round(0.39 * (words / sentences) + 11.8 * \
                  (syllables / words) - 15.59))

# Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")   