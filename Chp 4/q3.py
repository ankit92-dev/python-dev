#Print the lements of the list using a loop

#1. Using While loop
list=[1,4,9,16,25,36,49,64,81,100]
#print(list[0])
i=0  #Sets index postio 0
n=len(list) #Stores lenth of list i.e. no of elements
while i<n:
    print(list[i])
    i+=1     #Increment index postion
    
#2.Using for loop
list2=[1,4,9,16,25,36,49,64,81,100]
for num in list2:
    print(num)

#This one was easier and efficient using for loop