#Tuple is immutable unlike list which is mutable 
tup=(1,2,3,4,5)
#Get sepecific value using index postion
print(tup[0])
print(tup[4])
print(type(tup))

"""
#Mutating/Changi is not allowed in tuple
Eg:.
tup[0]=5  #0 is idx postion, 5 is no to be assiglned
#Empty tupe is valid
Eg:
tup=()
print(tup)
"""
tup2=(1,) #It is single element valid tuple
print(type(tup2),tup2)

#Putting "," is necessary; otherwise, Python considers it as an int or float
#Eg:
tup3=(1)
print(type(tup3),tup3)
tup4=(2.0)
print(type(tup4),tup4)