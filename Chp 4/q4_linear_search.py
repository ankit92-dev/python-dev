#Search for a number , in this tuple using loop 

#1. Using "while" loop
print("Using while loop: ")
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 100
i = 0
#i<len(tup) was added to make sure it don't loop infinitely incase x in not in tuple and x will never be equal to tup[i]
while i < len(tup) and x != tup[i]:  # Keep searching until found or end of tuple
    #print("Finding...")
    i += 1

#If and else was added so that if number is not found in tuple and it exits the loop what would it print
if i < len(tup):  # Check if we found the number in the list
    print("Found at idx: ", i)
else:
    print("Number in list")  # Case when x is not in the tuple
    
    
#2. Using "for" loop
print("Using for loop: ")
tup2 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
idx=0
for num in tup2:
    if x == num:
        print("Found at idx: ",idx)  # Prints only once when x is found
        break
    idx+=1
else:
    print("Not found")  # Runs only if x isn't found in the tuple
        
    
