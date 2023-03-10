'''
Homework 4-2
Name: Zachary Pace
Date: 3/9/2023
Description: finding all phone numbers and emails in text from clipboard
'''

import clipboard as c
import re

# Reading the clipboard
Document = c.paste()

# Creating List of Phone Numbers and Emails
phoneNumList = re.findall('\(?\d{3}\)?-\d{3}-\d{4}', Document)
EmailList = re.findall('\w+@\w+.\w+', Document)

# Print to command line
print("\nPhone Numbers found:\n" + str(phoneNumList))
print("\nEmails found:\n" + str(EmailList))

# Moved to Clipboard
c.copy("\nPhone Numbers found:\n" + str(phoneNumList) + "\n\nEmails found:\n" + str(EmailList))
print("\nLists copied to clipboard.")
