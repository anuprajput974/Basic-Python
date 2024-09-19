phones={
    "john" : 98764,
    "Ria"  : 98632,
    "Joy"  : 67353
}

print(phones)

print(len(phones))        # to print length 

print(type(phones))         # to print type

print(phones["john"])       # to access item of dict

print(phones.get("john"))     # to access item of dict

phones["john"]=89765          # to update value in dict
print(phones)


phones["kia"]=23456            # to add a element in dic
print(phones)


more_phones={                      # to add a now dic to existing one
    "jimmy": 83333
}
phones.update(more_phones)
print(phones)

phones.pop("john")                     # to remove a element from a dict
print(phones)

phones.popitem()                      # to  remove last element from a dict
print(phones)

#phones.clear()
print(phones)                           # this will empty the dict


for x in phones.items():                 # for traversing
    print(x)