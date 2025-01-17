"""
Author:  Ryan Gwin
Date written: 01/15/2025
Assignment:   Module1 exercise2 part2
Short Desc:  Write a program in cube.py that takes the length of an edge (an integer) 
            as input and prints the cube’s surface area as output. 
            For this exercise, write a program that contains an introductory docstring. 
            This documentation should describe what the program will do (analysis) 
            and how it will do it (design the program in the form of a pseudocode algorithm). 
            Include suitable prompts for all inputs, and label all outputs appropriately. 
            After you have coded a program, be sure to test it with a reasonable set of legitimate inputs.
"""

def cube():
    intCubeEdge = input("Enter the length of edge of the cube as an integer: ")
    surfaceArea = 6 * (int(intCubeEdge) ** 2)
    
    print("The surface area of the cube is: " + str(surfaceArea))
    
    """
    Finds the surface area of a cube with a given length.
    To find the surface area of a cube, the length of one edge is measured. 
    The length is squared to find the area of a single face.
    Then that number is multiplied by the number of faces on a cube, which is 6.
    
    Pseudocode:    
    DEFINITIONS
        INT intCubeEdge
        INT surfaceArea
        
    FUNCTION cube
        intCubeEdge = INPUT("Enter the length of edge of the cube as an integer: ")
        surfaceArea = (length ^ 2) * 6     
        OUTPUT "Surface area of the cube is: " + surfaceArea
    """

cube()