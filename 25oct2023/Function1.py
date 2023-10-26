list1 =[1,2,8,9,3,4,5]
# list.sort(reverse=True)
# list.extend([98,99])
# print (list)

# list5=[]
# for i in list:
#    a= i**2
#    list5.append(a)
# print(list5)
#
# res= lambda a:a**2
# print(res(3))

res = list(map(lambda a:a**2,list1))
print (res)
