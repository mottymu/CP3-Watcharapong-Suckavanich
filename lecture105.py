# OOP Class Inhesrit Example

class Vehicle:
    licenseCode = ""
    serialCode = ""

    def turnOnAirConditioner(self):
        print("Turn on : Air")


class Car(Vehicle):
    def sayHello(self):
        print("Hello World")


class PiclUp(Vehicle):
    pass


class Van(Vehicle):
    pass


class Estatecar(Vehicle):
    pass


car1 = Car()
car1.turnOnAirConditioner()
car1.sayHello()

pickup1 = PiclUp()
pickup1.turnOnAirConditioner()

van1 = Van()
van1.turnOnAirConditioner()

estatecar1 = Estatecar()
estatecar1.turnOnAirConditioner()