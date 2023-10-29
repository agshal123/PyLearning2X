# Python program to count the number of strings in a list where the string length is 2 or more and
# the first and last character are the same.


list1 = [1, 2, "ihalini", "rivar", "Pun"]
count = 0
for i in list1:
    print(type(i))
    if type(i) == str and len(i)>2 and i[0]==i[-1]:
        print(len(i))
        count += 1
    else:
        print(f"{i} is not string")
print(count)

