print("Enter three numbers:\n")
n1=int((input("Enter first number:\t")))
n2=int((input("Enter second number:\t")))
n3=int((input("Enter third number:\t")))

if(n1>n2 and n1>n3):
    print(n1, "is greatest")

elif(n2>n3 and n2>n1):
    print(n2, "is greatest")
else:
    print(n3,"is greatest")
