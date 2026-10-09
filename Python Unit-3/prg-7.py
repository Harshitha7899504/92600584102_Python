#7.Write a program to copy move and delete files  using shutil module.

import shutil
import os

# Create a sample file
with open("sample.txt", "w") as file:
    file.write("This is a sample file.")


shutil.copy("sample.txt", "copy.txt")
print("File copied successfully.")


shutil.move("copy.txt", "moved.txt")
print("File moved successfully.")


os.remove("moved.txt")
print("File deleted successfully.")
