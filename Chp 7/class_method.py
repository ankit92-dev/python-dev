"""
What is a Class Method?

A class method is a method that:
Works with the class itself, not an instance.
Takes cls (not self) as its first parameter.
Is defined using the @classmethod decorator.

"""
"""
# Syntax

class MyClass:
    @classmethod
    def my_class_method(cls, args):
        # method body
        pass
"""
#Example:

class Student:
    school_name = "Greenwood High"  # class variable (Common to all objects)

    def __init__(self, name):
        self.name = name

    @classmethod  #Class method starts here
    def change_school(cls, new_name):
        cls.school_name = new_name

    def display(self):
        print(f"Student: {self.name}, School: {Student.school_name}")

# Using the class
s1 = Student("Alice")
s2 = Student("Bob")

s1.display()  # Student: Alice, School: Greenwood High
s2.display()  # Student: Bob, School: Greenwood High

# Change the school name using class method
Student.change_school("Sunrise Public School")

s1.display()  # Student: Alice, School: Sunrise Public School
s2.display()  # Student: Bob, School: Sunrise Public School