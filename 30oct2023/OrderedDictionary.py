from collections import OrderedDict
od =OrderedDict()
od['a']=95
od['c']=78
od['b']=97
od['d']=100
print(od)

od['c']=od['b']
print(od.values())

key_list=list(od)
print(key_list)

value_list=list(od.values())
print(value_list[1])

for k,v in od.items():
    print(k,v)

print(dir(dict()))

pop_itm = od.pop("a")
print(pop_itm)

print(od)