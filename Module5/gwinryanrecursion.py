"""
Author: Ryan Gwin
Date Written: 02/16/2025

Description:
Recursion to print each element in a sequence, and tracks arguments.

"""
def printAll(seq):
    """
    Recursively prints each element in a sequence while tracking arguments.
    
    Parameters:
    seq (sequence): a list, tuple, or string to be printed element by element.
    """
    if seq:
        print(f"({seq}) -> {seq[0]}")
        printAll(seq[1:])

#testing the function
printAll([1, 2, 3, 4, 5])  
printAll([3,4,5,6,7,8,9,10])
printAll([10, 11, 12, 13, 14, 15])
