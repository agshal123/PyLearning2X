'''1. Create a program that takes two numbers as input and
prints whether the first number is greater than, less than, or equal to the second number.

'''

'''a = int(input("Enter first number\n"))
b= int(input("enter second number\n"))

if(a>b):
    print(f"{a} is greater than {b}")
elif(a<b):
    print(f"{a} is less than {b}")
else :
    print(f"{a} is equal to {b}")'''

a1 = int(input("Enter first number\n"))
b1 = int(input("enter second number\n"))
result ="greater than" if a1>b1 else "less than" if a1<b1 else "equal to"
print(f"{a1} is {result} {b1}")