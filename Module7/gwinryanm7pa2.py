"""
Assignment: Programming Assignment Part 2
Date Written: 03/01/2025
Author:  Ryan Gwin

Description:  Create an Employee class with name and employee number attributes, including accessor and mutator methods.

Create a ProductionWorker class as a subclass of Employee, with additional attributes for hourly pay rate and shift number.

Instantiate a ProductionWorker object with user-provided details and display the information to the screen.
"""

class Employee:
    def __init__(self, name, employee_number):
        self.__name = name
        self.__employee_number = employee_number

    #getters
    def get_name(self):
        return self.__name

    def get_employee_number(self):
        return self.__employee_number

    #setters
    def set_name(self, name):
        self.__name = name

    def set_employee_number(self, employee_number):
        self.__employee_number = employee_number

class ProductionWorker(Employee):
    def __init__(self, name, employee_number, hourly_pay_rate, shift_number):
        super().__init__(name, employee_number)
        self.__hourly_pay_rate = hourly_pay_rate
        self.__shift_number = shift_number

    #getters
    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate

    def get_shift_number(self):
        return self.__shift_number

    #setters
    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    #helper
    def get_shift_description(self):
        return "Day Shift (1)" if self.__shift_number == 1 else "Night Shift (2)"

#create production worker object
def main():
    #get user input
    name = input("Enter employee's name: ")
    employee_number = input("Enter employee number: ")
    hourly_pay_rate = float(input("Enter hourly pay rate: "))
    
    #ensure either 1 shift or 2 shifts
    while True:
        shift_number = int(input("Enter shift number (1 for Day, 2 for Night): "))
        if shift_number in [1, 2]:
            break
        print("Invalid shift number. Please enter 1 or 2.")

    #instantiate productionworker object
    worker = ProductionWorker(name, employee_number, hourly_pay_rate, shift_number)

    #display worker details
    print("\nEmployee Details:")
    print(f"Name: {worker.get_name()}")
    print(f"Employee Number: {worker.get_employee_number()}")
    print(f"Hourly Pay Rate: ${worker.get_hourly_pay_rate():.2f}")
    print(f"Shift: {worker.get_shift_description()}")

if __name__ == "__main__":
    main()