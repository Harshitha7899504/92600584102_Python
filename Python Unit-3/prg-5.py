#5.Write a program to display current date and time using datetime module.

import datetime

# Get current date and time
now = datetime.datetime.now()

print("Current Date and Time:", now)
print("Current Date:", now.date())
print("Current Time:", now.time())
