#7.Write a program to demonstrate list dictionary and set comprehensions.

# List comprehension
numbers = [1, 2, 3, 4, 5,6]
squares = [n * n for n in numbers]

print("List comprehension:", squares)

# Dictionary comprehension
square_dict = {n: n * n for n in numbers}

print("Dictionary comprehension:", square_dict)

# Set comprehension
even_set = {n for n in numbers if n % 2 == 0}

print("Set comprehension:", even_set)
