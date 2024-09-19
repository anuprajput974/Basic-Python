name1='college wallah'
name2="    physics wallah    "
name3='''MBA                              
         wallah'''                    # triple quote is used to print string in next line

print(name1,name2,name3)

print(type(name1))                   #type of string

print(name1[2])                           # indexing in a string

print(name1[:4])

for i in name1:                          # traversing using for loop
    print(i)

print(len(name2))      

name4=name2.upper()                       # for converting characters to uppercase
print(name4)

print(name3.lower())                       # for converting lower case to upper case

print(name2.capitalize())                   # to capitalize the first letter of string


print(name2.strip())                        # to remove the additional white spaces before the string


str1="hello world what a beautyful world this is "
print(str1.replace("world","earth",1))                    # use to replace some word in string, number is written that how many times to replace


list=str1.split( )                                       #used for splitting string
print(list)


print(name1+name2)                                       # used for concatination


student_name="aman"                                       # string formatting
student_marks=90

info=("this students name is {s}, and his marks are {m}".format(s=student_name,m=student_marks))
print(info)

print(str1.find('au'))                               # to find a character