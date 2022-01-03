# Nested Loop Example

"""
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
..
..
2 x 12 = 24
"""

"""
print("2 x 1 = 2")
print("2 x 2 = 4")
print("2 x 3 = 6")
print("2 x 4 = 8")
print("2 x 5 = 10")
print("2 x 6 = 12")
print("2 x 7 = 14")
print("2 x 8 = 16")
print("2 x 9 = 18")
print("2 x 10 = 20")
print("2 x 11 = 22")
print("2 x 12 = 24")
print("3 x 1 = 3")
print("3 x 2 = 6")
print("3 x 12 = 36")
print("4 x 1 = 4")
print("4 x 2 = 8")
print("4 x 12 = 48")
"""

"""
x = 1
y = 2*x
print("2 x", x, "=", y)
x = x + 1
y = 2*x
print("2 x", x, "=", y)
x = x + 1
y = 2*x
print("2 x", x, "=", y)
"""

"""
for x in range(12):
    x = x + 1
    y = 2 * x
    print("2 x", x, "=", y)
"""

"""
for x in range(12):
    print("2 x", x + 1, "=", 2 * (x + 1))

for x in range(12):
    print("3 x", x + 1, "=", 3 * (x + 1))

for x in range(12):
    print("4 x", x + 1, "=", 4 * (x + 1))
"""

for x in range(12):
    for y in range(12):
        print(x + 1, "x", y + 1, "=", (x + 1) * (y + 1))
