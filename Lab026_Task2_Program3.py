'''2. Use the ternary operator to find the maximum of three numbers entered by the user.

3. Develop a Python script that calculates the square and cube of a given number.'''

a = input("Enter first number\n")
b = input("enter 2nd number\n")
c= input("enter 3rd number\n")

if a>b and a>c:
    max =a
elif b>c:
    max = b
else:
    max =c
print(max)
