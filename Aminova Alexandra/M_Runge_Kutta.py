from sympy import *

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

t,y = symbols('t y')
N = 4
dt = 0.1
t0 = 0
t1 = 1
y0 = 1

F = t*(y**0.5)

def M_Runge_Kutta (t0, t1, y0, dt, F):
    Y = [y0]
    T = [t0]
    k = [ 0 for i in range(N)]
    for i in range(int((t1 - t0) / dt)):
        k[0] = F.subs([(y, Y[-1]), (t, T[-1])])
        k[1] = F.subs([(y, Y[-1] + dt*k[0]*0.5), (t, T[-1] + dt*0.5)])
        k[2] = F.subs([(y, Y[-1] + dt*k[1]*0.5), (t, T[-1] + dt*0.5)])
        k[3] = F.subs([(y, Y[-1] + dt*k[2]), (t, T[-1] + dt)])
        Y.append(Y[-1] + dt*(k[0] + 2*k[1] + 2*k[2] + k[3])/6)
        T.append(T[-1] + dt)
    plt.plot(T, Y)
    x = np.linspace(t0, t1, int((t1 - t0) / dt))
    plt.plot(x, ((4 + x**2)**2)/16)
    plt.xlabel('t')
    plt.ylabel('y')
    plt.show()

M_Runge_Kutta (t0, t1, y0, dt, F)
    
        