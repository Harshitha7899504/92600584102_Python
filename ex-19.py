#9.  Write a program to demonstrate iterators and iterables in Python.


numbers = [10, 20, 30, 40,50]


iterator = iter(numbers)

print("Using iterator:")
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


print("\nUsing iterator in a loop:")

iterator = iter(numbers)

for value in iterator:
    print(value)
