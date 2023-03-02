class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAirconitioner(self):
        print("Turn On : Air Con.")

class Car(Vehicle):
    def sayHello(self):
        print("Hi there!")
class PickUp(Vehicle):
    def color(self):
        colorName = ""
        print(self.colorName)
class Van(Vehicle):
    pass
class EstatCar(Vehicle):
    pass

car1 = Car()
car1.turnOnAirconitioner()
#car1.sayHello()
pickUp1 = PickUp()
pickUp1.turnOnAirconitioner()
#pickUp1.colorName = "Gold"
#pickUp1.color()
van1 = Van()
van1.turnOnAirconitioner()
estatCar1 = EstatCar()
estatCar1.turnOnAirconitioner()