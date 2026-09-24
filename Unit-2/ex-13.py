#3. Write a program to generate a multiplication table using a for loop.

number = int(input("Enter a number: "))

print("Multiplication Table of", number)

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
