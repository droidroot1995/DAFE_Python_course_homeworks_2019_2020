'''Реализовать расчет производной для заданной
функции в точке из интервала  [𝑥0,𝑥1] , построить её график'''

from sympy import *

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x = symbols('x')

def f (expr, x0):
    X = np.linspace(0, 2*np.pi, 100)
    f = lambdify(x, expr, "numpy")
    f = f(X)
    plt.plot(X, f, label='expr')
    
    diff_expr = expr.diff(x)
    f = lambdify(x, diff_expr, "numpy")
    f = f(X)
    plt.plot(X, f, label='diff_expr')
    plt.xlabel('x')
    plt.ylabel('y') 
    plt.legend()
    plt.show()
    print("f'(x0) = ", diff_expr.subs(x, x0))
    

expr = x**2 * sin(x)
print(expr)
f(expr, np.pi)
expr = 2*x*sin(x) + x**2*cos(x)
print("f'(x0) = ", expr.subs(x, np.pi))