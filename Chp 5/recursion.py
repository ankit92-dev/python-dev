#It is a piece of code that can be called infinite times once it is defined, so no need to write whole thing again and again
#Eg: Here, "n" is a variable which represents the parameter and every time it is called it assign that value as value of n and then continues whole process.

#def func_name(parameter)
#Only func_name(argument)
def factorial(n): #n is parameter
    if n == 0 or n == 1: #base case
        return 1 # 0!=1,1!=1
    else:
        #n!=n*(n-1)!
        return n * factorial(n - 1) #recursive call
# n represents any arguments to be used in fuction

#How looping works?
#It keeps looping until base case is met.
  
#Calling the recursive function
m=int(input("Enter a number: "))
print(factorial(m)) # m becomes value of n,m is argument

#Calling it more times, as many times you want
print(factorial(3))
print(factorial(4))
print(factorial(6))
print(factorial(7))
print(factorial(8))
print(factorial(9))
