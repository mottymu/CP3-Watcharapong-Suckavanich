# Exercise 10

start = int(input("Start : "))
step = int(input("Step : "))
result = ""

"""
for i in range(5):
    print(start + step * i, end = " ")
"""

for i in range(5):
    result += str(start + step * i + 1)
    print(result)
