#3.Write a program to illustrate instance variables and class variables. 

class Student:
    college = "Marwadi University"

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Harshitha", 20)
s2 = Student("Priya", 21)

print("Student 1:", s1.name, s1.age)
print("Student 2:", s2.name, s2.age)
print("College:", Student.college)

