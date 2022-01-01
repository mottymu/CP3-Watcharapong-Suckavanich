# List EX1 Example

menuList = []
priceList = []


def showBill():
    print("----My Food----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number], "THB")
    print("----Total----")
    print(sum(priceList), "THB")


while True:
    menuName = input("Please Enter Menu : ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)
# print(menuList, priceList)

showBill()
