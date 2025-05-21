# 1. Multilevel Inheritance

# In multilevel inheritance, a class is derived from a class that is also derived from another class.

# Base class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print("Driving...")

# Derived from Vehicle
class Car(Vehicle):
    def honk(self):
        print("Beep beep!")

# Derived from Car (multilevel)
class ElectricCar(Car):
    def charge(self):
        print("Charging battery...")

ec = ElectricCar("Tesla")
ec.drive()      # Inherited from Vehicle
ec.honk()       # Inherited from Car
ec.charge()     # Own method
print(ec.brand) # Inherited attribute