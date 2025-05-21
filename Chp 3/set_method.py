#Set Methods
# Creating a set
mySet = {1, 2, 3, 4, 5}
print("Initial set:", mySet)

# Adding an element
mySet.add(6)
print("After adding 6:", mySet)

# Adding multiple elements
mySet.update([7, 8]) #Update means adding
print("After adding 7 and 8:", mySet)

# Removing an element (will raise error if not present)
mySet.remove(3)
print("After removing 3:", mySet)

"""
# Discarding an element (won’t raise error if not present)
mySet.discard(10)  # 10 is not in the set, but no error
print("After trying to discard 10 (not present):", mySet)
"""

# Popping an element (removes and returns an arbitrary element)
popped = mySet.pop() #This popps first element
print("Popped element:", popped)
print("Set after pop:", mySet)

# Clearing the set
mySet.clear()
print("Set after clear:", mySet)
#After clear it gives empty set