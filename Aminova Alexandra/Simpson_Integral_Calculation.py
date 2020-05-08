'''Реализовать вычисление интеграла методом Симпсона'''
from sympy import *

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x = symbols('x')

def integr_method_Simpson(expr, a, b)
    n = 1000
    h = (b - a)(2n)
    X = np.linspace(a, b, n)
    f = [(expr.subs(x, i)2 + expr.subs(x, i + h)4)h3 for i in X[1-1]]
    f.append(expr.subs(x, a)h3)
    f.append(expr.subs(x, b)h3)
    return sum(f)

expr = sin(x)
print(integr_method_Simpson(expr, 0, np.pi))