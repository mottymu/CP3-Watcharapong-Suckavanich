# Return Function Example 2

def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice * 7 / 100)
    return result


# print(vatCalculate(100))

# Homework

totalPrice = int(input("Please input Total Price (THB) : "))
print("Your Price included VAT is :", vatCalculate(totalPrice), "THB")
