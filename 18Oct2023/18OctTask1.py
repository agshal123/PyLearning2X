# Fibonacci Series

# 0,1,1,2,3,5,8,13

n =int(input("enter number"))
a=0
b=1
print(a)
print (b)
for i in range(2,n+1):
    c=a+b
    a=b
    b=c
    print(c)



