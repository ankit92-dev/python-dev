"""
It works almost exactly opposite to @staticmethod
Why?
1.It can access and modify/change or add class level attributes
2.It cannot access instance(i.e. constructor) attributes directly, but it can return instances with attributes via constructors.
3.Though it directly doesn't contain attributes, since it's a method
4.It act as alternative constructor,because it return instances with attributes (via constructor)

Quick Contrast:

Method Type	    First Parameter	    Can Access Instance (self)	    Can Access Class (cls)

Instance Method	   self	                 Yes	                    Yes (via self._class_)
(constructor)
Class Method	   cls	                 No	                        Yes
Static Method	   None	                 No	                        No
"""

class Product:
    company = "TechCorp"  # Class attribute

    def __init__(self, name):#Constructor
        self.name = name   # Instance attribute

    @classmethod
    def set_company(cls, new_name): #cls=class(it refers to class only, not self(object))
        cls.company = new_name  # Modifying class attribute

    # @classmethod
    # def create_with_default_name(cls):
    #     return cls("DefaultProduct")  # Returning an object with an attribute

print("Initial: ",Product.company)  # TechCorp
Product.set_company("InnoTech") #Using classmethod to change class attribute
print("Changed: ",Product.company)  # InnoTech

# p = Product.create_with_default_name()
# print(p.name)           # DefaultProduct