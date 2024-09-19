names={"riya","tia","mia"}


print(len(names))              # to print length of sets

for x in names:                  # to traverse the set
    print(x)

names.add("govind")    #to add a value 
print(names)

if "tia" in names:       #check if item is present or not
    print("yes")

names_list={"gaurav","rahul","amit","suraj"}    # add another sequence in a ste
names.update(names_list)
print(names)


names.remove("tia")      #remove a element from a set
print(names)

names.discard("rahi")    #this function will not throw an error if value is not present in the set
print(names)


s1={"a","b","c","d"}
s2={"e","f","g","h","a"}


s3=s1.union(s2)           #to add to lists
print(s3)

s1s2=s1.intersection(s2)    # find the common elements
print(s1s2)



s1.intersection_update(s2)   #keep only duplicates while joining
print(s1)

s1.symmetric_difference_update(s2)    #keep all values except duplicates
print(s1)


