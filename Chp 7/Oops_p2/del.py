"""
#Syntax:
del obj.attribute  (It deletes certain attribute of object of class)
del obj          (It deletes whole object itslef)
"""
#Example:-(complex from beginner_vs_complex.py)
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
#Deleting(del)
del car1.model  #This deletes name attribute from c1 object
del car2        #This deletes whole object itself,therefor it is called after this it will throw error, since it doesn't exist now 

#Checing after deleting (It throws error)
"""
print(car1.color)  # Blue
print(car1.model)  # C-Class

print(car2.color)  # Black
print(car2.model)  # E-Class
"""