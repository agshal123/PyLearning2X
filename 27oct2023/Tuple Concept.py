#Lab085 for tuple concept in Pramod's lesson

list =[1,2,5,3,4,5]
tuple=tuple(list)
print(tuple)

#Nested Tuple
tuple1 = ("Punit","Rivan","Shalini")
tuple2 = ("Mummy","Papa")
tuple3=(tuple1,tuple2)
print(tuple3)
print(tuple1[0])
print(tuple3[1][1])

#Search in Tuple

cities =("London","Paris","Switzerland")
print("Paris" in cities) # will return true if present
print ("Moscow" in cities)
