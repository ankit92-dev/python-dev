#Mercedes
# Class for A-Class
class AClass:
    model = "A-Class"
    color = "Blue"
    horsepower = "163 HP"
    price = "$35,000"

# Class for C-Class
class CClass:
    model = "C-Class"
    color = "Black"
    horsepower = "255 HP"
    price = "$45,000"

# Class for G-Wagon
class GWagon:
    model = "G-Class"
    color = "White"
    horsepower = "416 HP"
    price = "$135,000"

# Creating objects
car1 = AClass()
car2 = CClass()
car3 = GWagon()

# Accessing details using objects
print("Car 1 Details:")
print(car1.model)
print(car1.color)
print(car1.horsepower)
print(car1.price)

print("\nCar 2 Details:")
print(car2.model)
print(car2.color)
print(car2.horsepower)
print(car2.price)

print("\nCar 3 Details:")
print(car3.model)
print(car3.color)
print(car3.horsepower)
print(car3.price)