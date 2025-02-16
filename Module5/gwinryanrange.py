"""
Author: Ryan Gwin
Date Written: 02/16/2025

Description: 
recreate the range() function

"""





def myRange(start, stop=None, step=1):
    """
    A custom implementation of Python's range function that returns a list.
    
    Parameters:
    start (int): The starting value of the sequence.
    stop (int, optional): The stopping value of the sequence. Defaults to None.
    step (int, optional): The step value for iteration. Defaults to 1.
    
    Returns:
    list: A list of numbers generated according to the given parameters.
    """
    #adjust values based on number of arguments
    if stop is None:
        stop, start = start, 0 
    
    #generate the list manually
    result = []
    if step > 0:
        while start < stop:
            result.append(start)
            start += step
    else:
        while start > stop:
            result.append(start)
            start += step
    
    return result

#testing the function
print(myRange(10))  
print(myRange(1, 10)) 
print(myRange(1, 10, 2))  
