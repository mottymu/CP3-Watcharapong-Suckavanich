# OOP Class Example

class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added Product to ", self.name, self.lastname, "'s cart")

customer1 = Customer()
customer1.name = "Wach"
customer1.lastname = "S"
customer1.addCart()

customer2 = Customer()
customer2.name = "Wan"
customer2.lastname = "M"
customer2.addCart()

customer3 = Customer()
customer3.name = "Nam"
customer3.lastname = "S"
customer3.addCart()

customer4 = Customer()
customer4.name = "Angpao"
customer4.lastname = "L"
customer4.addCart()