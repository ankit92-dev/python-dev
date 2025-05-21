from datetime import date
#input
name = input("Enteryour name:")
yob =int(input("Enter your year of birth:"))
#Calculate age
cy = date.today().year
age = cy - yob
#Output
print(f"{name} is {age} years old")