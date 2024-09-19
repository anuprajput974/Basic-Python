
n=int(input("enter the value of n"))
def sumOneToN():
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum


print(sumOneToN())

