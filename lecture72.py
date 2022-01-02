# List EX2 Example

menuList = []


def showBill():
    print("----My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1], "THB")
    print("----Total----")
  #  print(sum(menuList[:1]), "THB")


while True:
    menuName = input("Please Enter Menu : ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append([menuName, menuPrice])

# print(menuList, priceList)

showBill()
print(menuList)