'''greatest between 3 numbers'''

num1=int(input("enter the frst number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))

if num1>num2 and num1>num3:
    print(num1,"num1 is greatest")
elif num2>num3 and num2>num1:
    print(num2,"num2 is greatest")
else:
    print(num3,"num3 is greatest")
