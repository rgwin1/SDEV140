"""
Author: Ryan Gwin
Date Written: 01/26/2025
Assignment: Module2 Practice Exercise 3-10

Insructions: 
The credit plan at TidBit Computer Store specifies a 10% down payment and an annual interest rate of 12%. Monthly payments are 5% of the listed purchase price, minus the down payment.

Write a program in a file named tidbit.py that takes the purchase price as input. The program should display a table, with appropriate headers, of a payment schedule for the lifetime of the loan. Each row of the table should contain the following items:

- the month number (beginning with 1)
- the current total balance owed
- the interest owed for that month
- the amount of principal owed for that month
- the payment for that month
- the balance remaining after payment

The amount of interest for a month is equal to balance *  rate / 12. The amount of principal for a month is equal to the monthly payment minus the interest owed. 
"""


#declare variables
month = 1
annualRate = 0.12
monthlyRate = annualRate / 12
downPaymentRate = 0.1
tableFormatString = "%2d%15.2f%15.2f%17.2f%17.2f%17.2f" 
monthlyPaymentRate = 0.05

#get input from user, fltPurchaseprice
fltPurchasePrice = input("Enter the original purchase price: ")

#type check, make sure user input is a float, this is a function definition (DONT FORGET DOCSTRING)
def isFloat(fltPurchasePrice):
    """
    Converts user input from string to float
    if user input isn't able to be converted to float,
    sends an error message and returns false for use in the while loop
    """

    try: 
        #convert user input into floating point value
        fltPurchasePrice = float(fltPurchasePrice)
        return fltPurchasePrice
    
    except ValueError:
        print('Value not a pricepoint. Please enter price point in the format 0.00')
        #returns false in order to use in while loop
        return False

#create first instance of floating put if user puts in a float first
fltPurchasePrice = isFloat(fltPurchasePrice); 
   
#prevent user from entering string values
while (isFloat(fltPurchasePrice) == False):
     fltPurchasePrice = input("Please enter the price in the format 0.00: ")
     fltPurchasePrice = isFloat(fltPurchasePrice)
     
#create header
headerRow = "Month\t Starting\t Interest\t  Principal\t    Payment\t Ending Balance"
print(headerRow)
print("_______________________________________________________________________________________________________")

#get starting variables
balance = fltPurchasePrice - (fltPurchasePrice * downPaymentRate)
monthlyPayment = monthlyPaymentRate * fltPurchasePrice

#start iterating until balance = 0
while balance > 0:
    #get the last payment iteration
    if monthlyPayment > balance:
        monthlyPayment = balance
        interest = 0

    #all but the last iteration    
    else:
        interest = balance * monthlyRate
    #get principal and remaining after iteration
    principal = monthlyPayment - interest
    remaining = balance - principal

    #output in tabular format
    formattedRow = tableFormatString % (month, balance, interest, principal, monthlyPayment, remaining)
    print(formattedRow)

    #setup variables for next iteration
    balance = remaining
    month += 1






