# Program to find largest number in a list

list1=[]

#Method1
def large(list2):
    a=max(list2)
    return a

b = input("Enter how many numbers\n")
d=int(b)
for i in range(0,d):
    c=int(input("enter the number"))
    list1.append(c)
print(list1)
lar_num=large(list1)
print(f"largest of the list is {lar_num}")

#Method2 using Lambda expression
lar_num1=lambda list1:max(list1)
print(f"largets in the list is {lar_num1(list1)}")


