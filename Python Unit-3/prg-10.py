#10.Write a program to extract specific information from a text file using regular expressions.

import re

# Open and read the text file
with open("data.txt", "r") as file:
    text = file.read()

# Extract email addresses
emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)

# Extract 10-digit phone numbers
phones = re.findall(r'\b\d{10}\b', text)

print("Email Addresses:")
for email in emails:
    print(email)

print("\nPhone Numbers:")
for phone in phones:
    print(phone)
