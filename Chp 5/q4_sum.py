#Waf to print sum of "n" numbers using recursion
n=int(input("Enter a number: "))
def natural(sum):
    if sum==0:
        return 0 #Base case, it return 0 when n=0, so only 0 is added in the sum
    return natural(sum-1) + sum #This return act else return this
           
#Call
print(natural(n))


#Why return 0
"""
sum(5) = sum(4) + 5
sum(4) = sum(3) + 4
sum(3) = sum(2) + 3
sum(2) = sum(1) + 2
sum(1) = sum(0) + 1
sum(0) = 0  <-- Base case!
"""