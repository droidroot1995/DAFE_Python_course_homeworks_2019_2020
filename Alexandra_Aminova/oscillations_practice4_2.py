%matplotlib inline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import integrate
import math as m
import scipy.linalg as la
import scipy.sparse.linalg as sla

''' Исследуйте свободные колебания системы, состоящей из двух связанных осцилляторов.
    Вычислите зависимости для начальных условий'''

N = 2
_m = [1, 1]
k = [1, 1, 1]
R0 = np.array([0.5, 0])
v0 = np.array([0, 0])

omega = np.zeros((N+1, N), dtype=np.float64)

for alpha in range(N+1):
    for beta in range(N):
        omega[alpha, beta] = k[alpha]/_m[beta]
        
Omega = np.zeros((N, N), dtype=np.float64)

for i in range(N):
    if i == 0:
        Omega[i, i] = omega[0, 0] + omega[1, 0]
        Omega[0, 1] = -omega[1, 0]
        
    if i > 0:
        if i < N-1:
            Omega[i, i-1] = -omega[i, i]
            Omega[i,i] = omega[i, i] + omega[i+1, i]
            Omega[i, i+1] = -omega[i+1, i]
        else:
            Omega[i, i-1] = -omega[i, i]
            Omega[i, i] = omega[i, i] + omega[i+1, i]
            
Theta, Sigma = np.linalg.eig(Omega)

Theta = np.sqrt(Theta)
SigmaV = np.zeros((N, N), dtype=np.float64)

for i in range(N):
    for j in range(N):
        SigmaV[j, i] = -Theta[i]*Sigma[j, i]
        
C1 = np.dot(np.linalg.inv(Sigma),R0[None].T.conj())
C2 = np.dot(np.linalg.inv(SigmaV),v0[None].T.conj())

C = np.sqrt(C1**2 + C2**2)

alpha = np.zeros(N, dtype=np.float64)

for i in range(N):
    if C[i] == 0:
        alpha[i] = 0
    else:
        alpha[i] = np.arctan(C2[i]/C1[i])
        
        if C1[i] < 0:
            alpha[i] = m.pi + alpha[i]
            
        if C1[i] > 0:
            if C2[i] < 0:
                alpha[i] = 2*m.pi+alpha[i]

N = len(Omega)
N1 = 214
Tmax = 80
t = np.zeros(N1, dtype=np.float64)

X = np.zeros((N, N1), dtype=np.float64)
Xv = np.zeros((N, N1), dtype=np.float64)

for j in range(N1):
    t[j] = (j-1)/(N1-1)*Tmax
    
for j in range(N1):
    s = np.zeros(N, dtype=np.float64)
    
    for i in range(N):
        s = s+ C[i]*Sigma[:,i]*np.cos(Theta[i]*t[j] + alpha[i])
        
    X[:, j] = s
    
for j in range(N1):
    s = np.zeros(N, dtype=np.float64)
    
    for i in range(N):
        s = s+ C[i]*Sigma[:,i]*Theta[i]*np.sin(Theta[i]*t[j] + alpha[i])
        
    Xv[:, j] = -s
    
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
p1 = ax1.plot(t, X[0],'r--', t, X[1],'g')

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
p2 = ax2.plot(t, Xv[0],'r--', t, Xv[1],'g')

fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
p3 = ax3.plot(X[0], Xv[0])

fig4 = plt.figure()
ax4 = fig4.add_subplot(111)
p4 = ax4.plot(X[1], Xv[1])

c1 = np.fft.fft(X[0])
c2 = np.fft.fft(X[1])

Cm1 = np.zeros(N1//2, dtype=np.float64)
Cm2 = np.zeros(N1//2, dtype=np.float64)
Freq = np.zeros(N1//2, dtype=np.float64)

for j in range(1, N1//2):
    Cm1[j-1] = abs(c1[j-1])/(N1/2)
    Cm2[j-1] = abs(c2[j-1])/(N1/2)
    Freq[j-1] = (j-1)/Tmax

fig6 = plt.figure()
ax6 = fig6.add_subplot(111)
ax6.set_xscale('log')
ax6.set_yscale('log')
p6 = ax6.plot(Freq, Cm1,'r--', Freq, Cm2,'g')
