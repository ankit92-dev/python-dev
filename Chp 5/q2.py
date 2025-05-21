#Waf to print the elements of a list in a single line not as a list (list is the parameter)
marvel=["ironman","thor","batman","hulk"]
def sup_heroes(list):
    i=0  #i=idx postion
    while i<len(list):
        print(list[i],end=" ") #end="space" helps to print in same line
        i+=1                   #end="\n" helps print each element in new line

#Call
sup_heroes(marvel)

#Extra
print("\n")
#Using for loop
def sup_heroes(list):
    for el in list:
        print(el,end=" ")
#Call
sup_heroes(marvel)
