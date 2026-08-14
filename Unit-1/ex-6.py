#Write a program to illustrate the use of tuples and sets with basic operations.


print("\n----TUPLE OPERATIONS----")
t = (10, 20, 30, 40, 50)

print("Tuple:", t)
print("First element:", t[0])
print("Last element:", t[-1])
print("Length of tuple:", len(t))
print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))


print("\n----SET OPERATIONS----")
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Set1:", set1)
print("Set2:", set2)


set1.add(70)
print("Set1:", set1)


set1.remove(20)
print("Set1:", set1)


print("Union:", set1.union(set2))


print("Intersection:", set1.intersection(set2))


print("Difference (Set1 - Set2):", set1.difference(set2))
