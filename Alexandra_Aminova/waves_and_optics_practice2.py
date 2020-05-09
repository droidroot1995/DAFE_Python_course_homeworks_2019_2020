%matplotlib inline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import integrate
import math as m
import scipy.linalg as la
import scipy.sparse.linalg as sla

''' На практике ширина реальных щелей гораздо больше длины волны,
    поэтому более адекватной является модель, в которой щель рассматривается
    как набор когерентных источников сферических волн (принцип Гюйгенса)

    Рассчитайте распределение интенсивности света с длиной волны 5*10^-4 mm
    от одной щели конечного размера, заменяя его 20 точечными источниками,
    отстоящими друг от друга на 0.001 mm.
    Определите ширину центрального пика интенсивности при L = 200 mm.
    Как соотносится ширина центрального пика с шириной щели?'''

def Intensity1(Lambda, N, A, R0, r, Nb):
    
    Rr= np.zeros(N, dtype=np.float64)
    f = np.zeros(Nb, dtype=np.float64)
    
    for i in range(N):
        Rr[i] = np.linalg.norm(r - R0[:,i])
        
    for i in range(Nb):
        su = 0
        
        for j in range(N):
            su += (A[j]/Rr[j]*np.cos(2*np.pi/Lambda*Rr[j]-2*np.pi/Nb*i))
        f[i] = su**2
        
    return np.mean(f)
    
N = 20
A = [1 for i in range(N)]
Lambda = 5e-4

a = 0.001
R = np.zeros((3,N))
for i in range(N):
    R[2, i] = -((N/2) - 0.5)*a + i*a

Np = 201
z_min = -7
z_max = 7

z = np.zeros(Np, dtype=np.float64)

for i in range(Np):
    z[i] = z_min + (z_max - z_min)/(Np - 1)*(i)
    
L = 200
Nb = 3
I1 = np.zeros(Np, dtype=np.float64)

for i in range(Np):
    r = np.array([0, L, z[i]]).T
    I1[i] = Intensity1(Lambda, N, A, R, r, Nb)
    
I1max = np.amax(I1)
fig8 = plt.figure()
ax8 = fig8.add_subplot(111)
p8 = ax8.plot(z, I1/I1max)

width = 0
for i in range(Np):
    if I1[i] < 2.5e-7:
        width = i - width
        print (i)
print('width (ширинa центрального пика интенсивности) = %.2f mm' % float(width*14/200))
print("gap's width = ", N*0.001, 'mm')
