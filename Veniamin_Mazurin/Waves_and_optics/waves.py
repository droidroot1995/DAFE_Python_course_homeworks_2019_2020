%matplotlib inline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import integrate
import math as m
import scipy.linalg as la
import scipy.sparse.linalg as sla

def Wave(A, T, x):
    return A*np.cos(2 * np.pi/T * x)

def WaveP(A, T, x, v, t):
    return Wave(A,T, x-v*t)

def WaveN(A, T, x, v, t):
    return Wave(A,T, x+v*t)

x_min = -2*np.pi
x_max = 2*np.pi
Nx = 101

x = []

for i in range(Nx):
    x.append(x_min + (x_max - x_min)/(Nx-1)*(i))
    
t_min = 0
t_max = 50
v = 0.05
Nt = 101
T = 2* np.pi

t = []

for j in range(Nt):
    t.append(t_min + ((t_max - t_min)/(Nt - 1))*(j))
    
M1 = np.zeros((Nt, Nx), dtype=np.float64)
M2 = np.zeros((Nt, Nx), dtype=np.float64)

for i in range(Nt):
    for j in range(Nx):
        M1[i, j] = WaveP(1,T, x[j], v, t[i])
        M2[i, j] = WaveN(1,T, x[j], v, t[i])
        
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
p1 = ax1.plot(x, M1[0,:],'r--', x, M1[39,:],'g', x, M1[79,:],'b')

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
p2 = ax2.plot(x, M2[0,:],'r--', x, M2[39,:],'g', x, M2[79,:],'b')

X, Y = np.meshgrid(x, t)

fig3 = plt.figure()
ax3 = fig3.add_subplot(111, projection='3d')
p3 = ax3.plot_surface(X, Y, M1)

fig4 = plt.figure()
ax4 = fig4.add_subplot(111, projection='3d')
p4 = ax4.plot_surface(X, Y, M2)

fig5 = plt.figure()
ax5 = fig5.add_subplot(111)
p5 = ax5.contourf(M1, 15)

fig6 = plt.figure()
ax6 = fig6.add_subplot(111)
p6 = ax6.contourf(M2, 15)

