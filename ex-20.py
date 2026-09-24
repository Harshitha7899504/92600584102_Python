#20.Write a program to generate a sequence of numbers using generator functions and yield keyword.

def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

# Calling the generator
numbers = generate_numbers(5)

for num in numbers:
    print(num)
