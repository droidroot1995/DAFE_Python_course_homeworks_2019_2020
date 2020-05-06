import numpy as np
def fun(x):
       return x*x

def rectangle_int(fun, a, b ,n):
    dx = (b - a) / n
    x = a
    sum = 0
    for i in range(n):
        sum += dx * fun(x)
        x += dx
    return sum

x = fun(x)
print (rectangle_int(fun, 1, 10, 100))
