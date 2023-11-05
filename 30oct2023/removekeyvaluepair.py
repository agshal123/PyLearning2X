#Remove a key-value pair from the dictionary.

dict1 = {"Name1" :"Shalini", "Name2":"Punit","Name3":"Rivan"}
print (dict1)

removed_item = dict1.pop("Name1")
print(removed_item)
print(dict1)
print(len(dict1))