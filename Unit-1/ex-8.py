#8.Write a program to explain mutable and immutable objects in Python. 

# Immutable object: Integer
a = 10
print("Original value of a:", a)

# Trying to change the value creates a new object
a = 20
print("New value of a:", a)

# Mutable object: List
numbers = [10, 20, 30]
print("\nOriginal list:", numbers)

# Modifying the list changes the same object
numbers.append(40)
print("After adding an element:", numbers)

numbers[0] = 100
print("After changing an element:", numbers)

# Another example of immutable object: String
text = "Harshitha"
print("\nOriginal string:", text)

text = text + " Priya"
print("New string:", text)

# Another example of mutable object: Dictionary
student = {"name": "Swaroopa", "age": 18}
print("\nOriginal dictionary:", student)

student["age"] = 21
student["course"] = "Python"
print("Modified dictionary:", student)


