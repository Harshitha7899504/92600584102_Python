#2. Write a program to demonstrate different import mechanisms in Python.

# 1. Import the complete module
import math

print("1. Using import module:")
print("Square root of 25 =", math.sqrt(25))


# 2. Import a specific function
from math import factorial

print("\n2. Using from module import function:")
print("Factorial of 5 =", factorial(5))


# 3. Import multiple functions
from math import pow, ceil

print("\n3. Importing multiple functions:")
print("2 raised to 3 =", pow(2, 3))
print("Ceiling of 4.3 =", ceil(4.3))


# 4. Import module with an alias
import math as m

print("\n4. Using import with alias:")
print("Value of PI =", m.pi)


# 5. Import function with an alias
from math import sqrt as s

print("\n5. Using function with alias:")
print("Square root of 49 =", s(49))
