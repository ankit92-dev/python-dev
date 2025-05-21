#List Methods
#Methods and functions are different

list=[2,1,3]
print(list)

#Append, it adds element to list
#print(list.append(4)), It returns "none"
list.append(4)
#Sorts, it sorts list in ascending order
list.sort()
print(list)
#Sort reverse, it sorts list in descending order
list.sort(reverse=True)
print(list)
#Reverse, it reverse the list
list.reverse()
print(list)
#Insert, inserting an element at specific index position
#list.insert(idx_postion,element)
list.insert(3,9)
print(list)
#Remove, it remove specific elements directly
#4 is directly elemtnt of list
list.remove(4)
print(list)
#Pop, it removes an elments using index position
list.pop(3)
print(list)
#Here, 3 is index positon, not element itself
