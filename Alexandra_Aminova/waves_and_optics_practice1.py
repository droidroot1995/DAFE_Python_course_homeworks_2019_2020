%matplotlib inline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import integrate
import math as m
import scipy.linalg as la
import scipy.sparse.linalg as sla

''' Замените функцию ехр() на cos.
    Проанализируйте поведение решений волнового уравнения для различных лямбда'''

def Wave(A, x, lambda_):
    return A*np.cos(x*2*np.pi/lambda_)

def WaveP(A, x, v, t, lambda_):
    return Wave(A, x-v*t, lambda_)

def WaveN(A, x, v, t, lambda_):
    return Wave(A, x+v*t, lambda_)

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

t = []

for j in range(Nt):
    t.append(t_min + ((t_max - t_min)/(Nt - 1))*(j))
    
lambda_1 = 2
lambda_2 = 5

M1P = np.zeros((Nt, Nx), dtype=np.float64)
M1N = np.zeros((Nt, Nx), dtype=np.float64)
M2P = np.zeros((Nt, Nx), dtype=np.float64)
M2N = np.zeros((Nt, Nx), dtype=np.float64)

for i in range(Nt):
    for j in range(Nx):
        M1P[i, j] = WaveP(1, x[j], v, t[i], lambda_1)
        M1N[i, j] = WaveN(1, x[j], v, t[i], lambda_1)
        M2P[i, j] = WaveP(1, x[j], v, t[i], lambda_2)
        M2N[i, j] = WaveN(1, x[j], v, t[i], lambda_2)
        
fig1 = plt.figure()
ax1 = fig1.add_subplot(221)
p1 = ax1.plot(x, M1P[0,:],'r--', x, M1P[39,:],'g', x, M1P[79,:],'b')
ax1_1 = fig1.add_subplot(222)
p1_1 = ax1_1.plot(x, M1N[0,:],'r--', x, M1N[39,:],'g', x, M1N[79,:],'b')

fig2 = plt.figure()
ax2 = fig2.add_subplot(221)
p2 = ax2.plot(x, M2P[0,:],'r--', x, M2P[39,:],'g', x, M2P[79,:],'b')
ax2_1 = fig2.add_subplot(222)
p2_1 = ax2_1.plot(x, M2N[0,:],'r--', x, M2N[39,:],'g', x, M2N[79,:],'b')

X, Y = np.meshgrid(x, t)

fig3 = plt.figure()
ax3 = fig3.add_subplot(221, projection='3d')
p3 = ax3.plot_surface(X, Y, M1P)
ax3_1 = fig3.add_subplot(222, projection='3d')
p3_1 = ax3_1.plot_surface(X, Y, M1N)

fig4 = plt.figure()
ax4 = fig4.add_subplot(221, projection='3d')
p4 = ax4.plot_surface(X, Y, M2P)
ax4_1 = fig4.add_subplot(222, projection='3d')
p4_1 = ax4_1.plot_surface(X, Y, M2N)

fig5 = plt.figure()
ax5 = fig5.add_subplot(221)
p5 = ax5.contourf(M1P, 15)
ax5_1 = fig5.add_subplot(222)
p5_1 = ax5_1.contourf(M1N, 15)

fig6 = plt.figure()
ax6 = fig6.add_subplot(221)
p6 = ax6.contourf(M2P, 15)
ax6_1 = fig6.add_subplot(222)
p6_1 = ax6_1.contourf(M2N, 15)

'''Рассмотрите решение волнового уравнения при t = 0.
    Чему равен период функции, называемый длиной волны?

    Рассмотрите решение волнового уравнения при x = 0.
    Чему равен период функции, называемый периодом волны?

    Убедитесь в том, что отношение длины волны к периоду волны равно скорости распространения волны v'''

lambda_1exp = []
m = min(M1N[0,:])
for i in range(Nx):
    if (M1N[0,i] - m == 0):
        lambda_1exp.append(i)
print('lambda = %.2f' % float((lambda_1exp[1] - lambda_1exp[0])*4*np.pi/100))
        
T_1exp = []
m = max(M1N[:,0])
for i in range(Nt):
    if (abs(m - M1N[i,0]) == 0):
        T_1exp.append(i)
print('T = %.2f' % float((T_1exp[1] - T_1exp[0])*50/100))
                     
print('v_experimental = %.2f' % float((lambda_1exp[1] - lambda_1exp[0])*4*np.pi/((T_1exp[1] - T_1exp[0])*50)))
print('v_theory = %.2f' % v)
