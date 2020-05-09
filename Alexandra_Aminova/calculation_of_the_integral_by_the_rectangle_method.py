'''Реализовать вычисление интеграла методом прямоугольников'''

from sympy import *
import numpy as np

x = symbols('x')

def integr_middle_rects(expr, a, b):
    N = 1000
    h = (b - a)/N
    X = np.linspace(a, b, N)
    f = [expr.subs(x, i - 0.5*h) * h for i in X][1:]
    return sum(f)

def integr_middle_rects_2(x0, x1, n):
    h = (x1 - x0)/n
    x = np.arange(x0, x1, h)
    f = np.sin(np.pi* ((x - 0.5*h)**2)/2)    # f  = sin(0.5*pi*x**2)
    #f = np.sin(x - 0.5*h)
    f = f.tolist()
    return sum(f)*h

expr = x**2
print(integr_middle_rects(expr, 0, 1))
print(integr_middle_rects_2(0, 3.14, 1000))