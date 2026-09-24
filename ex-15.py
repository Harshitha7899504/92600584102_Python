#5. Write a program to demonstrate the use of break continue and pass statements.

# Demonstration of break
print("Using break:")
for i in range(1, 6):
    if i == 4:
        break
    print(i)

# Demonstration of continue
print("\nUsing continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Demonstration of pass
print("\nUsing pass:")
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
