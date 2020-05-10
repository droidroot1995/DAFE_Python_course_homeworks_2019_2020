import matplotlib
import numpy as np
import matplotlib.pyplot as plt


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

def trapezoid_int(fun, a, b, n):
    dx = 1.0 * (b - a) / n
    sum = 0.5 * (fun(a) + fun(b))
    for i in range(1, n):
        sum += fun(a + i * dx)
        return sum * dx

def simpson_int(fun, a, b, n):
    if n%2 == 1:
        n += 1
    dx = 1.0 * (b - a) / n
    sum = (fun(a) + 4 * fun(a + dx) + fun(b))
    for i in range(1, n // 2):
        sum += 2 * fun(a + (2 * i) * dx) + 4 * fun(a + (2 * i + 1) * dx)
        return sum * dx / 3


x = np.arange(-10, 10, 0.2)
y = fun(x)
fig, axs = plt.subplots()
plt.axis([-10, 10, - 10, 10])
plt.scatter(x, y)
plt.show()
