"""
1. Class Attributes

Shared across all instances of a class.
Defined "inside the class, but outside any instance methods(i.e.function)".
Useful for "constants" or values common to every instance.

2. Object Attributes (Instance Attributes)

"Unique" to each instance.
Defined using self inside methods (typically _init_).
Used for storing data specific to an object.
"""

class Dog:
    species = "Canis familiaris"  # class attribute , (species will be same to all dogs)

    def __init__(self, name):
        self.name = name  # object attribute, (it's inside fuction,so name will be unique to each dog)

d1 = Dog("Fido")
d2 = Dog("Buddy")

print("Same species,class attributes: ")
print(d1.species)  # Canis familiaris
print(d2.species)  # Canis familiaris

print("Unique name,object attributes: ")
print(d1.name)
print(d2.name)