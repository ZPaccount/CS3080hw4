'''
Homework 4-3
Name: Zachary Pace
Date: 3/9/2023
Description: using Regex to validate password
'''

# Import
import re

# While loop until a valid password is found
password = ""
valid = False
while not valid:
    password = input("\nPlease enter your password:")
    # Series of tests length -> lowercase -> uppercase -> number
    if len(password) >= 8:
        if re.search("[a-z]", password):
            if re.search("[A-Z]", password):
                if re.search("[0-9]", password):
                    valid = True
    # Prints error if still invalid
    if valid is False:
        print("Insecure Password, Try again.")

# Confirms Password is secure
print("\n" + str(password) + " is Secure.")
