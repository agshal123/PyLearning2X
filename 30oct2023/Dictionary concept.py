# Dictionary

dict_1=dict(Name="Shalini",Age=24)
print(dict_1)

dict_2 ={"Name": 'Shalini', "Age":24}
print(dict_2)

print (dict_1["Name"])
print (dict_1.keys())
print(dict_1.values())

value_list=list(dict_1.values()) # to print values of the dictionary
print(value_list[1])

key_list = list(dict_1.keys())
print (key_list[1])

# for iterations in dictionaries
for k,v in dict_1.items():
    print(k,v)


