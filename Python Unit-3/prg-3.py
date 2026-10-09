#3.Write a program to perform mathematical operations using math module.

import math

num = float(input("Enter a number: "))

# Mathematical operations
print("Square root =", math.sqrt(num))
print("Power (number^2) =", math.pow(num, 2))
print("Ceiling value =", math.ceil(num))
print("Floor value =", math.floor(num))
print("Absolute value =", math.fabs(num))
print("Factorial =", math.factorial(int(num)))

# Trigonometric operations
angle = float(input("Enter angle in degrees: "))
radian = math.radians(angle)

print("Sine =", math.sin(radian))
print("Cosine =", math.cos(radian))
print("Tangent =", math.tan(radian))
