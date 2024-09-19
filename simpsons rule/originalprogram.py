import numpy as np              # here we import numpy alias np because it is use for numerical camputation
def f(x):                       # here we define the given function f(x) which is given in the function
    return x * np.sin(x)        
def fun(f, a, b, n):            #here we defines the parameter of the function where f is the function,a is the lower limit,b is the upper limit and n is the subintervals to define the function into
    if n%2 != 0:                 # we have to check wheter the intervals completly divide by 2 because to apply simpsons 1/3 rule the number of intervals musrt be even
        print("n must be even")
    h = (b-a)/n                 # here we calculate the value of h 
    x = np.linspace(a, b, n+1)   # here we go through each value in the function
    y = f(x)                    # here we define y as the function
    integral = y[0] + y[n]       #applying 1/3 rule formula and storing first and last value in integral 
    for i in range(1, n, 2):     #iterating from 2nd value with a differnce of 2 till the before last one and all the value 
        integral += 4*y[i]  
    for i in range(2, n-1, 2):
        integral += 2*y[i]  
    integral *= h / 3
    return integral
a = 0
b = np.pi
n = 8
answer = fun(f, a, b, n)
print("the value is", answer)
