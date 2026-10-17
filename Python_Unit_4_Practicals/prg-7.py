#7.Write a program to illustrate method resolution order and magic methods.

# Demonstration of MRO
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

obj = D()
obj.show()

print("MRO:", [cls.__name__ for cls in D.mro()])


# Demonstration of Magic Methods
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Student Name: " + self.name

s = Student("Harshitha")
print(s)
