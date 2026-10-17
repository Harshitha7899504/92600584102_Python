#10.
f = open("sample.txt", "w")
f.write("Hello Python")
f.close()

f = open("sample.txt", "r")

print("Current position:", f.tell())

data = f.read(5)
print("Read data:", data)

print("Current position:", f.tell())

f.seek(0)
print("Position after seek:", f.tell())

print("Complete data:", f.read())

f.close()
