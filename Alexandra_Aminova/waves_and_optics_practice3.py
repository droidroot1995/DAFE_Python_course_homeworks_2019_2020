%matplotlib inline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import integrate
import math as m
import scipy.linalg as la
import scipy.sparse.linalg as sla

'''Исследуйте распределение интенсивности света при интерференции на системе двух щелей,
    используя модель щели конечной ширины.'''

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
    
def Intensity2(Lambda, N, A, R0, r, Nb, d, as_):
    
    Rr1= np.zeros(N, dtype=np.float64)
    Rr2= np.zeros(N, dtype=np.float64)
    f = np.zeros(Nb, dtype=np.float64)
    
    for i in range(N):
        Rr1[i] = np.linalg.norm(r - R0[:,i])
        Rr2[i] = np.linalg.norm(r - R0[:,N + i])
        
    for i in range(Nb):
        su = 0
        
        for j in range(N):
            su += ((A[j]/Rr1[j]*np.cos(2*np.pi/Lambda*Rr1[j]-2*np.pi/Nb*i)) + 
                  (A[j]/Rr2[j]*np.cos(2*np.pi/Lambda*Rr2[j]-2*np.pi/Nb*i))) * np.cos(np.pi*d*as_/(2*Lambda*L))
        f[i] = su**2
        
    return np.mean(f)
    
N = 20
A = [1 for i in range(N)]
Lambda = 5e-4

a = 0.0001
d = 0.1
R = np.zeros((3,2*N))
for i in range(0, N):
    R[2, i] = - (d - N*a) -(N - 1)*a + i*a
for i in range(0, N):
    R[2, N + i] = (d - N*a) + i*a    

Np = 201
z_min = -7
z_max = 7

z = np.zeros(Np, dtype=np.float64)

for i in range(Np):
    z[i] = z_min + (z_max - z_min)/(Np - 1)*(i)
    
L = 200
Nb = 3
I1 = np.zeros(Np, dtype=np.float64)
I2 = np.zeros(Np, dtype=np.float64)

for i in range(Np):
    r1 = np.array([0, L, z[i]]).T
    I1[i] = Intensity1(Lambda, N, A, R, r1, Nb)
    r2 = np.array([0, L, z[i]]).T
    I2[i] = Intensity2(Lambda, N, A, R, r1, Nb, d, N*a)
    
I1max = np.amax(I1)
I2max = np.amax(I2)

fig8 = plt.figure()
ax8 = fig8.add_subplot(111)
ax8.set_title('2 finit gaps')
p8 = ax8.plot(z, I1/I1max)

fig8_1 = plt.figure()
ax8_1 = fig8_1.add_subplot(111)
ax8_1.set_title('2 point gaps')
p8_1 = ax8_1.plot(z, I2/I2max)
