# Creating a nested dictionary
students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "grade": "A"
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "grade": "B"
    }
}

#Accessing whole dictionary
print(students)
# Accessing a specific value
print("Student1's Name:", students["student1"]["name"])
print("Student2's Grade:", students["student2"]["grade"])
"""
# Looping through nested dictionary
for student_id, info in students.items():
    print("\nID:", student_id)
    for key, value in info.items():
        print(key, ":", value)
"""