#4.Write a program to implement single multilevel and multiple inheritance.

# Single Inheritance
class A:
    def display_A(self):
        print("This is class A")

class B(A):
    def display_B(self):
        print("This is class B")

print("Single Inheritance:")
obj1 = B()
obj1.display_A()
obj1.display_B()

# Multilevel Inheritance
class C:
    def display_C(self):
        print("This is class C")

class D(C):
    def display_D(self):
        print("This is class D")

class E(D):
    def display_E(self):
        print("This is class E")

print("\nMultilevel Inheritance:")
obj2 = E()
obj2.display_C()
obj2.display_D()
obj2.display_E()

# Multiple Inheritance
class F:
    def display_F(self):
        print("This is class F")

class G:
    def display_G(self):
        print("This is class G")

class H(F, G):
    def display_H(self):
        print("This is class H")

print("\nMultiple Inheritance:")
obj3 = H()
obj3.display_F()
obj3.display_G()
obj3.display_H()
