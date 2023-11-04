#Write a Python program that takes two lists and returns True if they have at least one common member.
list1=[]
list2=[]

def compare(list1,list2):
    z=list1.intersection(list2)
    print(z)
    if z!=set():
        return True
    else:
        return False
    # if(list1 & list2):
    #     return True
    # else:
    #    return False

a=int(input("enter how many number in the list"))
for i in range(0,a):
    b=input("enter the number")
    list1.append(b)
print (list1)

c=int(input("enter how many number in the list"))
for i in range(0,c):
    d=input("enter the number")
    list2.append(d)
print (list2)

z=compare(set(list1),set(list2))
print (z)

#Method 2

z=list(filter(lambda list1,list2:"True" if set(list1).intersection(set(list2)) !=set() else "False" ))
print (z)




