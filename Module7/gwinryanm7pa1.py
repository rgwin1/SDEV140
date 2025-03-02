"""
Assignment: Programming Assignment Part 1
Date Written: 03/01/2025
Author:  Ryan Gwin

Description:  Create a Person class with name, address, and phone attributes, and a display info method

create a Customer class that is a subclass of Person, with attributes customer number, and mailing list

instantiate customer class object with information related to customer and display it to screen
"""

#person class
class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def display_info(self):
        return f"Name: {self.name}\nAddress: {self.address}\nPhone: {self.phone}"

#create customer subclass of person class
class Customer(Person):
    def __init__(self, name, address, phone, customer_number, mailing_list):
        super().__init__(name, address, phone)
        self.customer_number = customer_number
        self.mailing_list = mailing_list

    def display_info(self):
        mailing_status = "Yes" if self.mailing_list else "No"
        return f"{super().display_info()}\nCustomer Number: {self.customer_number}\nMailing List: {mailing_status}"


#customer instantiation
customer1 = Customer("John Doe", "123 Fake St, Fake City", "123-4567", "12345", True)
print(customer1.display_info())