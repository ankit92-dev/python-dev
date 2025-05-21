# Define an initial dictionary
myDict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# 1. myDict.keys() - returns all keys
print("Keys in myDict:")
print(myDict.keys())  # Output: dict_keys(['name', 'age', 'city'])

# 2. myDict.values() - returns all values
print("\nValues in myDict:")
print(myDict.values())  # Output: dict_values(['Alice', 25, 'New York'])

# 3. myDict.items() - returns all (key, value) pairs as tuples
print("\nKey-value pairs in myDict:")
a=print(myDict.items())  # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])
print(type(a))

# 4. myDict.get("key") - returns the value for the given key
print("\nGet value for key 'name':")
print(myDict.get("name"))  # Output: Alice

# Using get() with a non-existing key
print("\nGet value for non-existing key 'salary':")
print(myDict.get("salary", "Not found"))  # Output: Not found

# 5. myDict.update(newDict) - adds new key-value pairs or updates existing ones
#First make a newDict
newDict = {
    "age": 26,         # this will update the existing 'age'
    "salary": 50000    # this will be added as a new key
}
#Update or Add works  the same
myDict.update(newDict)
print("\nUpdated dictionary after using update():")
print(myDict)
# Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'salary': 50000}

#Or no newDict, directly update
myDict.update({"salary": 60000, "age": 27})
print(myDict)