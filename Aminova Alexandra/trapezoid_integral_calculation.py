'''Реализовать вычисление интеграла методом трапеции'''
from sympy import *

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def integr_method_trapeze(expr, a, b):
    n = 1000
    h = (b - a)/n
    X = np.linspace(a, b, n)
    f = [(expr.subs(x, i) +  expr.subs(x, i - h))*0.5 for i in X][1:]
    return sum(f)*h

expr = sin(x)
print(integr_method_trapeze(expr, 0, np.pi))