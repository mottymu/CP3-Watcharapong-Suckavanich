# OOP Class Encapsulation Example

class Animal():
    def eat(self):
        print("Eating Eating !")


class Cat(Animal):
    __name = ""

    def setName(self, text):
        self.name = text
        print("Setting New Cat Name = ", self.name)

    def eat(self):
        print("Meoww !!", self.name)


cat1 = Cat()
cat1.setName("TT")
cat1.eat()
