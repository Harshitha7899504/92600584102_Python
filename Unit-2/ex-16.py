#6. Write a program to iterate over lists strings and dictionaries using loops.


numbers = [10, 20, 30, 40, 50]

print("List elements:")
for num in numbers:
    print(num)


name = "Python"

print("\nString characters:")
for ch in name:
    print(ch)


student = {
    "name": "Priya",
    "age": 20,
    "course": "Python"
}

print("\nDictionary elements:")
for key, value in student.items():
    print(key, ":", value)
