#Factorial of "n" numbers using for loop
n=int(input("Enter a number: "))
fact=1
for i in range(1,n+1): # i ranges from 1 to n, [1,n]or[1,n+1)
    fact=fact*i
print(fact)