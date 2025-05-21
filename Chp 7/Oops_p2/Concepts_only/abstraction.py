#1. Abstraction
#Hiding the complex implementation and showing only essential features.

#Example:
from abc import ABC, abstractmethod
#ABC,(Abstract Base Class)
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

# Cannot create object of abstract class directly
# a = Animal()  # Error

d = Dog()
d.make_sound()  # Bark

"""
Key Points:
ABC and @abstractmethod come from the abc module.
"""
#Note:-
"""
1. ABC (Abstract Base Class):
Comes from the abc module.
It marks a class as abstract, meaning it’s not meant to be instantiated directly.
Used when you want to force subclasses to implement certain methods.

2. @abstractmethod:
Declares a method that must be overridden in any subclass.
Without it, a subclass might "forget" to implement the important methods.

"""