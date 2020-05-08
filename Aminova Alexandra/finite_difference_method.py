'''Реализовать численное решение уравнения теплопроводности с помощью метода конечных разностей
для представленного выше случая, построить график распределения температуры по толщине пластины.'''
from sympy import *

import numpy as np
import matplotlib
import matplotlib.pyplot as plt


Tl = 400
Tr = 600
T0 = 300
L = 0.1
lambda_ = 48
ro = 7800
C = 460
t1 = 60 

N_time = 21
N_x = 51
tau = t1 / N_time
h = L / N_x

A = lambda_ / h**2
B = 2*A + ro*C/tau
F = [0 for i in range(N_x)]

T = np.array([np.array([T0 for i in range(N_x)]) for k in range(N_time)])
#T = [T0 for i in range(N)]
for i in range(N_time):
    T[i][0] = Tl
    T[i][-1] = Tr

alpha = [ 0 for i in range(N_x) ]
beta = [ Tl for i in range(N_x) ]

for k in range (1, N_time):
    for i in range(0, N_x - 1):
        alpha[i + 1] = (A / (B - A * alpha[i]))
        F[i] = -ro*C*T[k - 1][i]/tau
        beta[i + 1] = (A*beta[i] - F[i])/(B - A*alpha[i])
    for i in range (N_x - 2, 0, -1):
        T[k][i] = alpha[i]*T[k][i + 1] + beta[i]

plt.matshow(T)
plt.colorbar()
plt.show()