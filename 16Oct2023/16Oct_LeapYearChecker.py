# program that determines whether a given year is a leap year.

year = int(input("Enter year in digits\n"))

if year % 4 == 0 and year % 100 != 0:
   #print(f"{Year} is a Leap Year")
    y="Leap Year"
elif year % 400 == 0:
    y = "Leap Year"
else:
    y = "Not a Leap Year"
print(f"{year} is {y}")
