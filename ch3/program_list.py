'''list=[23,65,19,90]
temp=list[0]
list[0]=list[2]
list[2]=temp
print(list)'''

n=int(input("enter the value of n"))
list=[]
for _ in range(n):
    num=int(input())
    list.append(num)

idx1=int(input("enter index 1"))
idx2=int(input("enter index 2"))

temp=list[idx1]
list[idx1]=list[idx2]
list[idx2]=temp

print(list)
