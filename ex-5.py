#5. Write a program to create and manipulate lists using indexing slicing and list comprehensions.

numbers=[10,20,30,40,50,60,70]
print("num:",numbers)

print("\n----List indexing----")
print(numbers[0])
print(numbers[0:8])
print(numbers[2])
print(numbers[-4])


print("\n----List Slicing----")
print(numbers[1:3])
print(numbers[0:7])
print(numbers[-2:])
print(numbers[::-1])


print("\n----List Manipulation----")
numbers.append(80)
print(numbers)
numbers.remove(50)
print(numbers)
numbers.insert(1,22)
print(numbers)


print("\n----List Comprehensions----")
squares=[x*x for x in numbers]
print("Squares:", squares)
even_numbers=[x for x in numbers if x%2==0]
print("Even numbers:", even_numbers)
