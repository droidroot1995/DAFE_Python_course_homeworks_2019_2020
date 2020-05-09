%matplotlib inline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import integrate
import math as m
import scipy.linalg as la
import scipy.sparse.linalg as sla

'''Проведите сравнительный анализ распределений интенсивности для L = 1 mm и L = 50 mm'''

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
    
L1 = 1
L2 = 50

Nb = 3
I1 = np.zeros(Np, dtype=np.float64)
I2 = np.zeros(Np, dtype=np.float64)

for i in range(Np):
    r1 = np.array([0, L1, z[i]]).T
    I1[i] = Intensity1(Lambda, N, A, R, r1, Nb)
    r2 = np.array([0, L2, z[i]]).T
    I2[i] = Intensity1(Lambda, N, A, R, r2, Nb)
    
I1max = np.amax(I1)
I2max = np.amax(I2)

fig8 = plt.figure()
ax8 = fig8.add_subplot(221)
ax8.set_title('L = 1 mm')
p8 = ax8.plot(z, I1/I1max)

ax8_1 = fig8.add_subplot(222)
ax8_1.set_title('L = 50 mm')
p8_1 = ax8_1.plot(z, I2/I2max)
