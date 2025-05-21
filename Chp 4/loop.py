#Loops in Python♤♡◇♧

#For loop
# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)
    
#While loop
# Print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1
    
#Continue and break
for i in range(1, 10):
    if i == 5:
        continue  # Skip number 5
    if i == 8:
        break     # Stop before number 8
    print(i)