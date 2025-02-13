"""
Author: Ryan Gwin
Date Written: 02/12/2025
Description:  
A function that takes total_sales as an argument, and returns the total sales tax (county and state).
County tax is 2.5% of total sales, and state is 5% of total sales.  
"""


def calculate_total_tax():
    """
    description:  calculates total tax from given total sales
    """
    total_sales = input("Enter the total sales for the month as a monetary value greater than $0.00: ")

    #defines try/except to validate user input. 
    def is_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False
    #validate user input.  If not float, then reprompt for user-input until float and greater than 0.00 
    if (is_float(total_sales) == True) and (float(total_sales) > 0):
        total_sales = float(total_sales)
    else:
        while (is_float(total_sales) == False) or (float(total_sales) <= 0):
            total_sales = input('Please enter total sales as a monetary value greater than $0.00: ')
        total_sales = float(total_sales)
    
    #after validation: calculate total tax
    county_tax_rate = 0.025
    state_tax_rate = 0.05
    county_tax = total_sales * county_tax_rate
    state_tax = total_sales * state_tax_rate
    total_tax = state_tax + county_tax 

    #print values to screen
    print(f"county tax: ${county_tax:.2f}")
    print(f"state tax: ${state_tax:.2f}")
    print(f"total tax: ${total_tax:.2f}")


calculate_total_tax()


