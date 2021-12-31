number = int(input("Please input number : "))
print(list(range(number, 0, -1)))

for x in range(number, 0, -1):
    print((x * ' ' + (number - x) * '*') + '*' + ((number - x) * '*') + (x * ' '))