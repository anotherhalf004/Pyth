dic= {
    "me" : "eng" ,
    "sis" : "doc"
}
# print(dic['notme']) # throws error if not exist in the dict
print(dic.get('notme')) # prints NONE

print(dic.keys())
print(dic.values())

for key in dic.keys():
    print(dic[key]) # it is ordered
    print(f'Key value pair : {key} - {dic[key]}')

# KEY VALUE pairs
print(dic.items())

for key,value in dic.items():
    print(f'key value pairs are : {key} - {value}')


# DICTIONARY METHODS 

d1 = {
    'A':'1',
    'B':'2',
    'C':'3',
    'D':'4'
}
d2={
    'S':'11',
    'W':'12',
    'Q':'13'
}
d1.update(d2) #all d2 to d1
d1.pop('W')
d2.popitem() # last one gets deleted i.e Q
print(d1)
print(d2)
# d2.clear()
# del d2  
del d2['S'] 
print(d2) 

empty= {}










