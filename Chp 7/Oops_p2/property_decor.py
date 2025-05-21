#1. Original Code (Without @property)
"""
class Student:
    def __initI_(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    def calcPercentage(self):
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(98, 97, 99)
print(stu1.percentage)   # Prints initial percentage

stu1.phy = 96            # Changed here
print(stu1.phy)
stu1.calcPercentage()    # Recalculate after change
print(stu1.percentage)

Problem with the Above Code:

If you update marks (e.g., phy), the percentage doesn’t update automatically.
You must manually call calcPercentage() again.
This leads to inconsistent or outdated data.
"""

#2. Improved Code (Using @property)

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property  #Now, it act an an attribute
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(98, 97, 99)
print(stu1.percentage)   # Automatically calculated

stu1.phy = 96            # Changed here
print(stu1.phy)
print(stu1.percentage)   # Automatically updated!

"""Advantages of Using @property:

Cleaner and automatic recalculation.

No need to manually update values.

Acts like an attribute, but has the power of a method."""