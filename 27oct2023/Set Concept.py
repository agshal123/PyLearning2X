list1 = [33,45,33,45,21]
list2=tuple(list1)
print(list2)

set2=set(list1)
print(set2)

#Union
Set1 ={1,2,3,4,5}
Set2 = {4,5,6,7,8}
set3=Set1.union(set2)
print(set3)

#Intersection
set4 = Set1.intersection(Set2)
print(set4)

#Difference

set5 = Set1.difference(Set2)
print(set5)

#Subset
set6 ={1,2}
set7 ={1,2,3,4,5}
subset = set6.issubset(set7)
print(subset)