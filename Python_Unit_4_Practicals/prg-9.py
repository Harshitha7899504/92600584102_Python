#9.
# Write data into a file
f = open("sample.txt", "w")
f.write("Hello, Python!\n")
f.write("File handling example.")
f.close()

# Read data from a file
f = open("sample.txt", "r")
print("File content:")
print(f.read())
f.close()

# Append data to a file
f = open("sample.txt", "a")
f.write("\nThis is appended data.")
f.close()

# Read updated data
f = open("sample.txt", "r")
print("\nUpdated file content:")
print(f.read())
f.close()
