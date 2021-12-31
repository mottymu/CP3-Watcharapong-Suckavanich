# Loop Example

"""
1
*
2
**
3
***
5
*****
"""

number = int(input("Please input number : "))
print(number * "*")
print("-----------")

for x in range(number):
    text = ""
    for y in range(x + 1):
        text += "*"
    print(text)
print("-----------")

for x in range(number):
    print("*" * (x + 1))
