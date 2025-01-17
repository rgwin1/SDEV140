"""

Author: Ryan Gwin
Date written: 01/17/2025
Assignment:   Module1 Programming Assignment Part2
Short Desc:  get restaurant bill pre-tax, pre-tip as user input, 
            calculate tax with rate of 7%, 
            calculate tip at 18%,
            add to bill for total bill
            print to screen


"""



def billCalculator():
    """ 
    This function takes user input, bill, calculates tax, calculates tip, 
    adds them together and prints to screen.
        
    """
    tipPercentage = 0.18
    taxRate = 0.07
    bill = input("What is the cost of the bill: ")
    tax = float(bill) * taxRate
    billWithTax = float(bill) + tax
    tip = billWithTax * tipPercentage
    total = round((billWithTax + tip), 2)
    print(f"Your total is ${total}.")
    

    

billCalculator()