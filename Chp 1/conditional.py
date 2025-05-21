n=int(input("Enter a number: "))
if n>0:                               
    print("Number is positive")
    #Nested if inside if
    #For this a tab or 4 spaces is needed to do
    if n%2==0:
        print("It is even")
    else:
        print("It is odd")
elif n<0:
    print("The number is negative")
else:
    print("The number is 0")