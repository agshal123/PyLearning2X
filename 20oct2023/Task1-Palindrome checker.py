# Palindrome checker

# 1st Method
# a = input("enter the string\n")
# a_len = int(len(a))
# print(a_len - 1)
# x= (a[::-1])
# print (x)
# if a==x:
#     print(f"{a} is palindrome")
# else:
#     print(f"{a} is not palindrome")

#2nd Method
# x=''
# for i in range(a_len - 1, -1, -1):
#     x = x+a[i]
# if a==x:
#     print(f"{a} is palindrome")
# else:
#     print(f"{a} is not palindrome")

#3rd Method

def pal_checker(a):
    a_len = int(len(a))
    print(a_len - 1)
    x = (a[::-1])
    return x

a = input("enter the string\n")
z= pal_checker(a)
if a==z:
    print(f"{a} is palindrome")
else:
    print(f"{a} is not palindrome")

