%matplotlib inline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import integrate
import math as m
import scipy.linalg as la
import scipy.sparse.linalg as sla

'''проведите сравнительный анализ траекторий луча
    для различных законов изменения коэффициента преломления'''

def CoeffRefraction(y):
    return (1+7*y**0.1)**7
def CoeffRefraction1(y):
    return (1+2*y)**2

y_min = 1e-4
y_max = 20
Np = 100

y = []

for i in range(Np):
    y.append(y_min + (y_max - y_min)/(Np-1)*(i))
    
Nk = 1000

Y = np.zeros(Nk, dtype=np.float64)
Z = np.zeros(Nk, dtype=np.float64)
Z1 = np.zeros(Nk, dtype=np.float64)

Xb = np.zeros(Np, dtype=np.float64)
Xb1 = np.zeros(Np, dtype=np.float64)
Yb = np.zeros(Np, dtype=np.float64)

for i in range(Np):
    for k in range(Nk):
        Y[k] = y_min + (y[i] - y_min)/(Nk -1)*(k)
        Z[k] = 1/((CoeffRefraction(Y[k])**2-1)**0.5)
        Z1[k] = 1/((CoeffRefraction1(Y[k])**2-1)**0.5)
        
    Xb[i] = np.trapz(Z, Y)
    Xb1[i] = np.trapz(Z1, Y)
    Yb[i] = Y[Nk-1]
    
fig12 = plt.figure()
ax12 = fig12.add_subplot(111)
ax12.set_title('(1+7*y**0.1)**7')
p12 = ax12.plot(Xb, Yb)

fig13 = plt.figure()
ax13 = fig13.add_subplot(111)
ax13.set_title('(1+2*y)**2')
p13 = ax13.plot(Xb1, Yb)
