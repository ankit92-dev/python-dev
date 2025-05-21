# 3. Inheritance
# One class (child) inherits properties and methods from another (parent).

#Example:
class Vehicle:    #Parent class
    def __init__(self, brand): #Constructors
        self.brand = brand

    def drive(self): #Normal,print function
        print("Driving...")
#class chil_class(parent_class    (Syntax)
class Car(Vehicle): #Child class (inheriting parent class)
    def honk(self):
        print("Beep beep!")

c = Car("Toyota")
c.drive()       # Inherited method
c.honk()        # Own method
print(c.brand)  # Inherited attribute

"""
Key Points:
Car inherits from Vehicle.
"""