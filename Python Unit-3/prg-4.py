#4.Write a program to generate random numbers using random module.

import random


print("Random integer:", random.randint(1, 100))


print("Random float:", random.random())


print("Random number between 10 and 50:", random.randint(10, 50))

numbers = [10, 20, 30, 40, 50]
print("Random choice:", random.choice(numbers))
