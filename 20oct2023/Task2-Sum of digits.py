# Create a function that calculates the sum of the digits of a positive integer.

# Method-1
# a = input("Enter any number")
# num_len = int(len(a))
# x = 0
#
# for i in range(0, num_len):
#     x = int(a[i]) + int(x)
# print(x)

#Method 2 using function

def add_dig(a,num_len):
    x=0
    for i in range(0, num_len):
        x = int(a[i]) + int(x)
    return x

a= input("Enter any number\n")
num_len = int(len(a))
x= add_dig(a,num_len)
print(f"sum of digits in {a} is {x}")