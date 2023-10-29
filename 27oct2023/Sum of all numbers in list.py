# Program to sum of all numbers in a list

list1=[]

#Mathod 1
def sumofnumbers(list2,d):
    a =0
    for i in range(0,d):
       a+=list2[i]
    return a

d=int(input("enter how many numbers\n"))
for i in range(0,d):
    e=int(input("enter the number\n"))
    list1.append(e)
print(list1)
output = sumofnumbers(list1,d)
print(output)


#Method 2
from functools import reduce
f = reduce(lambda x,y:x+y,list1)
print(f)
