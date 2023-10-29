# Program to multiply numbers in a list

list1=[]

def mulofnumbers(list2,d):
    a=1
    for i in range(0, d):
        a*=list2[i]
    return a

b= int(input("enter how many numbers\n"))
for i in range (0,b):
    c=int(input("enter the number\n"))
    list1.append(c)
print(list1)
mulofnumbers1=mulofnumbers(list1,b)
print(mulofnumbers1)

# Method 2 using reduce
from functools import reduce
output = reduce(lambda x,y:x*y,list1)
print(output)