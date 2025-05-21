#1.Print 1 to 100
#2.Print 100 to 1
#3.Multiplication table by user

#Using for and range

#1.
for i in range(1,101):
    print(i)
# #2.
# rev=[]
# for i in range(1,101):
#     rev.append(i)
#     print(i)
# r=rev.reverse()
# print(r)

#3.
n=int(input("Enter your number: "))
for i in range(1,11):
    print(n*i)