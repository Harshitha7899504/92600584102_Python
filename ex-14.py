#4.Write a program to find the sum of digits of a number using a while loop.

number = int(input("Enter a number: "))

number = abs(number)
sum_digits = 0

while number > 0:
    digit = number % 10
    sum_digits += digit
    number //= 10

print("Sum of digits =", sum_digits)
