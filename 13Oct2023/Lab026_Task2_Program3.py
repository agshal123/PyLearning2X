'''2. Use the ternary operator to find the maximum of three numbers entered by the user.

3. Develop a Python script that calculates the square and cube of a given number.'''

a = float(input("Enter first number\n"))
b = float(input("enter 2nd number\n"))
c = float(input("enter 3rd number\n"))

'''if a>b and a>c:
    max =a
elif b>c:
    max = b
else:
    max =c
print(max)'''

max = a if (a > b and b > c) else b if (b > c) else c
print(f"The maximum of{a},{b},{c} is {max}")
