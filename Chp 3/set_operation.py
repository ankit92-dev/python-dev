# Set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Set A:", A)
print("Set B:", B)

# Union
print("Union of A and B:", A.union(B))  # or A | B

# Intersection
print("Intersection of A and B:", A.intersection(B))  # or A & B

# Difference
#It returns whatever is unique in A that is not in B
print("Difference A - B:", A.difference(B))  # or A - B

# Symmetric Difference (items in A or B but not both)
#It removes common element
print("Symmetric Difference:", A.symmetric_difference(B))  # or A ^ B