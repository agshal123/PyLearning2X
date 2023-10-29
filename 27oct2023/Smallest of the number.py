# Program to find smallest number in list

list1=[]

def small(list2):
    a= min(list2)
    return a

a= int(input("enter how many numbers\n"))
for i in range(0,a):
    b=int(input("enter the number"))
    list1.append(b)
print(list1)
small_num=small(list1)
print(f"smallest in the list is {small_num}")

#Method 2 using Lambda Expression

Small_num1= lambda list1:min(list1)
print(Small_num1(list1))