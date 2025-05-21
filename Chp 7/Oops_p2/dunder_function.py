"""
What Are Dunder Functions? (__dunderfunc__)

Dunder functions (also called magic methods or special methods) are built-in Python methods that start and end with double underscores ().
They let you define how your objects behave with built-in functions and operators.


Common Dunder Functions:

Dunder Function	Purpose

__init__(self, ...):	    Constructor: Runs when you create a new object.
__str__(self):	            Defines the string representation (used by print).
__repr__(self):	        Official string representation (for debugging).
__len__(self):	            Defines behavior of len() on your object.
__getitem__(self, key):	Allows indexing (obj[key]).
__setitem__(self, key, value):	Allows item assignment (obj[key] = value).
__call__(self, ...):	    Makes the object callable like a function.
__add(self, other):	    Defines + operator. Similar for __sub, __mul_, etc.
__eq__(self, other):	    Defines == comparison.

"""

#Example:
class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"This dog is named {self.name}"

    def __len__(self):
        return len(self.name)

dog = Dog("Buddy")
print(dog)          # This dog is named Buddy
print(len(dog))     # 5