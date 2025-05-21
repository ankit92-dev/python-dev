#Sets
#Each set has unique values and are mutable, it's element is immutable'
# Creating a set
mySet = {1, 2, 3, 4, 5}
print("Initial set:", mySet)

# Sets automatically remove duplicates
dupSet = {1, 2, 2, 3, 4, 4}
print(dupSet) #During output it removes duplicate
print("Set with duplicates removed:", dupSet)