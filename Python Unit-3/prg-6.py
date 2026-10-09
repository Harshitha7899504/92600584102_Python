#6.Write a program to perform file and directory operations using os and sys modules.

import os
import sys

# Display current directory
print("Current Directory:", os.getcwd())

# Create a directory
if not os.path.exists("MyFolder"):
    os.mkdir("MyFolder")
    print("Directory created successfully.")


file_path = os.path.join("MyFolder", "sample.txt")

with open(file_path, "w") as file:
    file.write("Hello, this is a sample file.")

print("File created successfully.")

if os.path.exists(file_path):
    print("File exists.")


print("\nDirectory Contents:")
print(os.listdir())

print("\nPython Version:", sys.version)

print("Command-line Arguments:", sys.argv)
