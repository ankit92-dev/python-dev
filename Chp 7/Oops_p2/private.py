"""
#Private(attributes and methods):
Private attributes and methods are meant to be used only within the class and are not accessible from outside the class.
(i.e., not accesible using objects)

#Syntax:
self.__attribute=attribute  (i.e. "__",2 underscores before attribute)
"""
#Example:-
class Accout:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_passacc_pass=acc_pass #Made private
        
acc1=Accout("454534453453","pass34code")

print(acc1.acc_no)
#print(acc1.__acc_passacc_pass) This line throws error,since it doesn't allow to access "acc_pass " attribute