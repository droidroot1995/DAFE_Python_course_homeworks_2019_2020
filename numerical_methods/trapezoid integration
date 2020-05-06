def fun(x):
       return x*x

def trapezoid_int(fun, a, b, n):
    dx = 1.0 * (b - a) / n
    sum = 0.5 * (fun(a) + fun(b))
    for i in range(1, n):
        sum += fun(a + i * dx)

    return sum * dx

x = fun(x)
print (trapezoid_int(fun, 1, 10, 100))
