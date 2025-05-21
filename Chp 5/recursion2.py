#Recursion is a function which is advanced part of loop which calls itself multiple times and therefore act like a loop
#Recursion and loops are almost same thing, only difference recursion is less used only when it offers better optimization than loops
def show(n):
    if(n==0):  #base case, *required
        return #This exits the loop, avoids infinite loop
    print(n)
    show(n-1) ##This line calls it multiple times until base case is met
    
#Call
show(5) # 5,4=n-1,3=n-2,2=n-3,1