#9.Write a program to use re module functions  such as match search and findall.

import re

text = "Python is easy. Python is powerful. I love Python."

# 1. match()
result1 = re.match(r"Python", text)

if result1:
    print("match():", result1.group())
else:
    print("match(): Pattern not found")


# 2. search()
result2 = re.search(r"powerful", text)

if result2:
    print("search():", result2.group())
else:
    print("search(): Pattern not found")


# 3. findall()
result3 = re.findall(r"Python", text)

print("findall():", result3)
