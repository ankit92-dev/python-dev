"""
Beginner Version:
Acts like a pre-filled template.
Every object gets the same values (like color, model).
Easy to understand, but not flexible.

Complex Version (with _init_ and self):
## __init__:- act as constructor in python,initializes objects automatically on creation
Acts like a blueprint or constructor.
you can create many objects with their own unique values.
Very powerful and real-world style — this is how apps, games, and websites structure data.
"""


#1.Beginner:-  Without _init_ and self
class Car:
    color = "Red"
    model = "A-Class"
# Creating object
car1 = Car()

# Accessing data
print(car1.color)  # Red
print(car1.model)  # A-Class
"""
What’s happening:
1.You’re setting "fixed" values inside the class.
2.All objects will have the "same" color and model.
3.You can’t customize car1 or car2 easily.
"""


#2.Complex:- With "_init_" and "self"
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

# Creating object with "custom "values
car1 = Car("Blue", "C-Class")
car2 = Car("Black", "E-Class")

# Accessing data
print(car1.color)  # Blue
print(car1.model)  # C-Class

print(car2.color)  # Black
print(car2.model)  # E-Class
"""
What’s happening:
1._init_ is called automatically when the object is created.
2.self.color = color saves the color inside the object.
3.You can make as many unique cars as you want.
"""