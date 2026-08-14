#4.Write a program to demonstrate string operations including slicing formatting and built-in string functions.

text="Hello Python"
print("Original String:", text)


print("\n------String Slicing------")

print(" First 5 charecters:",text[:5])
print("charecter from index 3:",text[3:])
print("charecters from index 0 to 7:", text[0:8])
print("Reverse of String:", text[::-1])

print("\n------String Formatting-----")
name="Harshitha"
course="MCA"
print("My name is {} and I am studying {}.". format(name, course))
print(f"My name is {name} and I am studying {course}.")


print("\n-----Built-in string Functions-----")
text="Harshi Lucky"
print(len(text))
print(text.upper())
print(text.lower())
print(text.title())
print(text.replace("Harshi", "Harshitha"))
print(text.find("L"))
print(text.count("y"))
print(text.isalpha())
print(text.isalnum())

