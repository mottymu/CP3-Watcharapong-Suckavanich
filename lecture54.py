# Return Function Example 3

# Log in
def login():
    usernameInput = input("Username :")
    passwordInput = input("Password :")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print("Invalid Username or Password")
        return login()


# Show Menu
def showMenu():
    print("-----iShop-----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()


# Select Menu
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        totalPrice = int(input("Total Price (THB) :"))
        print(vatCalculate(totalPrice))
    elif userSelected == 2:
        print(priceCalculate())
    else:
        print("Please choose 1 or 2")
        menuSelect()

# VAT Calculator
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result


# Price Calculator
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)


#  Homework

login()
