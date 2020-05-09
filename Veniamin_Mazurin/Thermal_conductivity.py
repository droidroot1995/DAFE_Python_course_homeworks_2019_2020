%matplotlib inline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import integrate
import math as m
Nx=100
Nt=10000
a= 46/460/7800 #a=lambda / (C*p)
L= 0.1
t_max= 60
T=np.zeros((Nx,Nt))
x=np.linspace(0, L, num = Nx)
t=np.linspace(0, t_max, num = Nt)
dx= L/Nx
dt= t_max/ Nt
for i in range(1,Nx-1):
    T[i,0]= 300
for i in range(Nt):
    T[0, i] = 400
    T[Nx-1, i] = 600
for n in range(1,Nt):
    for i in range(1,Nx - 1):
        T[i,n]= T[i, n-1]+ a* dt* (T[i+1,n-1]+ T[i-1,n -1] -2* T[i, n-1])/ dx**2
        

print(T[:,Nt-1])
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
surf1 = ax1.plot(x, T[:,Nt-1])
   
