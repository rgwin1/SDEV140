"""
Author: Ryan Gwin
Date Written: 02/08/2025

Description: 
This program finds the top three most expensive items in a shop. 
It stores item prices in a dictionary, converts it into a sortable list, and sorts the list in descending order using a function. 
Finally, it prints the three most expensive items with their prices.
"""



#Sample data: Dictionary with items and their prices
shopItems = {'Apple': 0.50, 'Banana': 0.20, 'Mango': 0.99, 'Coconut': 2.99, 'Pineapple': 3.99}

#Convert dictionary items into a list of tuples
itemsList = list(shopItems.items())

#Function to get the price of an item (used for sorting)
def getPrice(item):
    return item[1]  

#Sort the list based on price in descending order
itemsList.sort(key=getPrice, reverse=True)

#Display the top three most expensive items
print("Top three most expensive items:")
for i in range(3):  
    print(itemsList[i][0], itemsList[i][1]) 
