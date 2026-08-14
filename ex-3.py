#3. Write a program to perfrom arithmetic relational and logical operations using Python operators.

print("-------Arithmetic Operations------")

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
        
print("Addition=", a+b)
print("Subtraction=", a-b)
print("Multiplication=", a*b)
print("Division=", a/b)
print("Modulus=", a%b)


print("\n------Relational Operations----")
print("a==b:", a==b)
print("a !=b:", a!=b)
print("a>b:", a>b)
print("a<b:", a<b)
print("a>=b:", a>=b)
print("<=b:", a<=b)
      

print("\n------Logical Operations------")
print("(a>0 and b>0):", a>0 and b>0)
print("(a<0 and b<0):", a<0 and b<0)
print("not (a>b):", not (a>b))
