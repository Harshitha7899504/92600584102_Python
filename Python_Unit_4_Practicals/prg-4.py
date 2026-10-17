#4.Write a program to demonstrate instance methods, class methods, and static methods.

class Student:
    college = "Marwadi University"

    def instance_method(self):
        print("This is an instance method.")

    @classmethod
    def class_method(cls):
        print("College:", cls.college)

    @staticmethod
    def static_method():
        print("This is a static method.")

s1 = Student()

s1.instance_method()
Student.class_method()
Student.static_method()
