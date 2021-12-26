# Exercise 8

# Products
product1Name = "Apple"
product1Price = 10
product2Name = "Orange"
product2Price = 15
product3Name = "Grape"
product3Price = 20
product4Name = "Mango"
product4Price = 12
product5Name = "Banana"
product5Price = 30

# Program
usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "admin" and passwordInput == "1234":
    print("Welcome Admin !")
    print("-----Mottymu Shop-----")
    print("-----Our Product List-----")
    print("1.", product1Name, "> Price (THB) : ", product1Price)
    print("2.", product2Name, "> Price (THB) : ", product2Price)
    print("3.", product3Name, "> Price (THB) : ", product3Price)
    print("4.", product4Name, "> Price (THB) : ", product4Price)
    print("5.", product5Name, "> Price (THB) : ", product5Price)
    userChoose = int(input("Please Choose Product >>  "))
    if userChoose == 1:
        print("You choose :", product1Name)
        userNeed = int(input("How many do you need? >>  "))
        print("---------------")
        print("Your Order is : ", product1Name)
        print("Price : ", product1Price, "THB")
        print("Amount : ", userNeed, "pcs")
        print("---------------")
        print("Total : ", product1Price * userNeed, "THB")
        print("---------------")
    elif userChoose == 2:
        print("You choose :", product2Name)
        userNeed = int(input("How many do you need? >>  "))
        print("---------------")
        print("Your Order is : ", product2Name)
        print("Price : ", product2Price, "THB")
        print("Amount : ", userNeed, "pcs")
        print("---------------")
        print("Total : ", product2Price * userNeed, "THB")
        print("---------------")
    elif userChoose == 3:
        print("You choose :", product3Name)
        userNeed = int(input("How many do you need? >>  "))
        print("---------------")
        print("Your Order is : ", product3Name)
        print("Price : ", product3Price, "THB")
        print("Amount : ", userNeed, "pcs")
        print("---------------")
        print("Total : ", product3Price * userNeed, "THB")
        print("---------------")
    elif userChoose == 4:
        print("You choose :", product4Name)
        userNeed = int(input("How many do you need? >>  "))
        print("---------------")
        print("Your Order is : ", product4Name)
        print("Price : ", product4Price, "THB")
        print("Amount : ", userNeed, "pcs")
        print("---------------")
        print("Total : ", product4Price * userNeed, "THB")
        print("---------------")
    elif userChoose == 5:
        print("You choose :", product5Name)
        userNeed = int(input("How many do you need? >>  "))
        print("---------------")
        print("Your Order is : ", product5Name)
        print("Price : ", product5Price, "THB")
        print("Amount : ", userNeed, "pcs")
        print("---------------")
        print("Total : ", product5Price * userNeed, "THB")
        print("---------------")
    else:
        print("Sorry ! We don't have more Product")

else:
    print("Wrong Username or Password")
