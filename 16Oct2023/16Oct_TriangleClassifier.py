# program that classifies a triangle based on its side lengths.

a = float(input("Enter the length of first side\n"))
b = float(input("Enter the length of second side\n"))
c = float(input("Enter the length of third side\n"))

if a==b==c:
    tri ="Equilateral Triangle"
elif (a==b and a!=c) or (b==c and b!=a) or (a==c and a!=b):
    tri = "Isosceles Triangle"
else:
    tri = "Scalene Triangle"
print(f"Traingle is {tri}")