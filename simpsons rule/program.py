import numpy as np


def f(x):
    return x * np.sin(x)

def composite_simpsons_one_third(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Number of subintervals must be even.")
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    integral = (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])
    return integral

a = 0 
b = np.pi 
n = 8  

approx_integral = composite_simpsons_one_third(f, a, b, n)
print("Approximate value of the integral:", approx_integral)
