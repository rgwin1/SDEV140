#program to take 3 inputs: name, phone number and address and displays them

#array of states for correct information check
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

#take input
firstName = input("Enter your first name: ");
lastName = input("Enter your last name: ");
fullName = firstName.capitalize() + " " + lastName.capitalize();


phoneNumber = input(str("Enter your 10-digit phone number (1234567890): "));
#error check: ensures strings are valid for information requested
while (len(phoneNumber) != 10) or (phoneNumber.isdigit() == False):
    print("Your phone number is either not 10 digits or contains letters. Please try again: ");
    phoneNumber = input(str("Enter your 10-digit phone number (1234567890): "));
    
streetAddress = input("Enter your street address: ");
city = input("Enter your city: ");
state = input("Enter your state, e.g. (IN): ").upper() ;

#error check: makes sure state provided is correct
while (state not in states):
    print("Invalid State Code: ");
    state = input("Enter your state, e.g. (IN): ");
        
zipCode = input(str("Enter your 5 digit zipcode: "));

#error check: make sure zipcode is valid
while len(zipCode) > 5 or (zipCode.isdigit() == False):
    print("Your zipcode is not 5 digits or it contains letters. Please only enter 5 digits.");
    zipCode = input(str("Enter your 5 digit zipcode: "));

#output inputs to console
print("Hello, " + fullName + ".");
print("Phonenumber: " + phoneNumber);
print("Address: " + streetAddress + ",\n\t " + city.capitalize() + ",\n\t " + state.upper() + ",\n\t " + zipCode);
