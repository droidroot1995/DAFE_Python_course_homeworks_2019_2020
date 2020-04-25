%matplotlib inline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import integrate
import math as m
import scipy.linalg as la
import scipy.sparse.linalg as sla
from scipy.signal import argrelextrema

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
A = np.ones(N)
Lambda = 5e-4
R0=np.zeros((N,3))
for i in range(N):
    R0[i]=np.array([[0, 0, 0.001 * i]])
R0 = R0.T

Np = 201
z_min = -15
z_max = 15

z = np.zeros(Np, dtype=np.float64)

for i in range(Np):
    z[i] = z_min + (z_max - z_min)/(Np - 1)*(i)
    
L = 200
Nb = 10
I1 = np.zeros(Np, dtype=np.float64)

for i in range(Np):
    r = np.array([0, L, z[i]]).T
    I1[i] = Intensity1(Lambda, N, A, R0, r, Nb)
    
I1max = np.amax(I1)
fig8 = plt.figure()
ax8 = fig8.add_subplot(111)
p8 = ax8.plot(z, I1/I1max)
i1min=argrelextrema(I1[ int(Np/2): ] , np.less)[0][0] # индекс минимума считается от начала среза
print( "The main maximum's width: ", 2*(z_max- z_min)/Np * i1min)
