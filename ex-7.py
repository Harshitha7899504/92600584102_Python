#7.Write a program to create a dictionary and demonstrate dictionary methods and iteration.

student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA",
    "marks": 85
}


print("student:", student)

print("\nName:", student["name"])
print("Marks:", student.get("marks"))

student["grade"] = "A"
print("\ngrade:", student)

student.update({"age": 21})
print("age:", student)

student.pop("marks")
print("marks:", student)

print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

print("\nIterating through dictionary:")
for key, value in student.items():
    print(key, ":", value)

if "name" in student:
    print("\n'name' key exists in the dictionary.")
