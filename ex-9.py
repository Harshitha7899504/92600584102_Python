#9. Write a program to define and use user-defined functions with different types of arguments.

# 1. Positional Arguments
def add(a, b):
    return a + b

print("Addition:", add(10, 20))


# 2. Keyword Arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=20, name="Harshitha")


# 3. Default Arguments
def greet(name="Student"):
    print("Hello,", name)

greet()
greet("Priya")


# 4. Variable-Length Arguments (*args)
def total(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

print("Total:", total(10, 20, 30, 40))


# 5. Variable-Length Keyword Arguments (**kwargs)
def display(**details):
    for key, value in details.items():
        print(key, ":", value)

display(name="Harita", age=21, course="MCA")
