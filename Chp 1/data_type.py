#Input
#All the value of input is a string
a=input("Enter your name: ")
b=input("Enter your age: ")
c=input("Enter a float: ")
# print(a,"\n",b,"\n",c)
print(type(a),a)
print(type(b),b)
print(type(c),c)

#After Casting
print("Casting: ")
#Casting is necessary when required to use it correctly especially while adding or working on numbers for <int>
a2=a
b2=int(b)
c2=float(c)
print(type(a2))
print(type(b2))
print(type(c2))

#Example
print("/n Example: ")
m=int(c2)
print(type(m),m)
add=b2 + m
print(add)