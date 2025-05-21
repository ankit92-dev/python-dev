#Q.Create student class that takes name and marks of 3 subjects as arguments in constructor/Then create a method to print the average
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def print_average(self): #Subclass
        print(sum(self.marks) / len(self.marks))

# Taking user input
name = input("Enter student's name: ")
marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(3)]

#Self call
s1 = Student(name, marks)
s1.print_average()  #Calling print subclass