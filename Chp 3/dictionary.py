# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Accessing specific values using keys
print("Name:", student["name"])
						#dict_name["key_name"]
print("Age:", student["age"])

# Adding a new key-value pair
#dict_name["key_name"]="value"
student["subject"] = "Math" #Appending
print("Updated Dictionary:", student)

# Updating a value
#i.e. key_value is mutable
student["grade"] = "A+"
print("After Grade Update:", student)

# Removing a key-value pair
del student["age"]
print("After Removing Age:", student)
# Looping through the dictionary
for key, value in student.items():
    print(key, ":", value)