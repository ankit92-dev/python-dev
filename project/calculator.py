#Calculator
def add(x,y):
    return x + y
def sub(x,y):
   if x>y:
       return x-y
   return y-x
def mult(x,y):
    return x*y
def div(x,y):
    if y==0:
        return "Cannot divide by zero"
    return x/y

print("Select operation: ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

#Choice
choice =input("Enter choice (1/2/3/4) ")

n1=float(input("Enter first number: "))
n2=float(input("Enter second number: "))

if choice=='1':
    print("Result: ",add(n1,n2))
elif choice=='2':
    print("Result: ",sub(n1,n2))
elif choice=='3':
    print("Result: ",mult(n1,n2))
elif choice=='4':
    print("Result: ",div(n1,n2))
else:
    print("Invalid input")
