"""
What is super()?
super() is a built-in function in Python used in inheritance.
It allows a child class to access methods and constructors from its parent class.

In the example:
super()._init_(type)
This lets child class to call and assign type to parent class.
"""
class Car:
    def __init__(self, type):
        self.type = type  # Assign the type of the car (e.g., electric, petrol)

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped.")

# Child class inheriting from Car
class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name  # ToyotaCar has an extra attribute 'name'
        super().__init__(type)  # Call parent class (Car) constructor to initialize 'type'

# Create an object of ToyotaCar
car1 = ToyotaCar("Prius", "Electric") #This only calls ToyotaCar(Child) class,but it saves type in Parent class

# Access attributes and methods
print("Name: ",car1.name)  # Output: Prius
print("Type: ",car1.type)  # Output: Electric
car1.start()      # Output: Car started...
car1.stop()       # Output: Car stopped.