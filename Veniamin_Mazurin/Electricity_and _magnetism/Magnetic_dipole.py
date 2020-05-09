#magnetic dipole
#Странный график, не могу найти ошибку
%matplotlib inline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import integrate
import math as m

def Bdipole( X, Y, M): # М- вектор магнитного момента
    Nx = len(X)
    Ny = len(Y)
    
    Bx = np.zeros((Nx, Ny))
    By = np.zeros((Nx, Ny))
    for i in range(Nx):
        for j in range(Ny):
            R= (X[i]**2 + Y[j]**2)**0.5
            Bx[i, j] =3* (M[0]*X[i]+ M[1]*Y[j])*X[i]/R**5 - M[0]/R**3
            By[i, j] =3* (M[0]*X[i]+ M[1]*Y[j])*Y[i]/R**5 - M[1]/R**3
    return Bx, By

R_0=1
N1=21
M=[0,1]
x_min = -5*R_0
y_min = -5*R_0

x_max = 5*R_0
y_max = 5*R_0

x = []
y = []
for i in range(N1):
    x.append(x_min+(x_max-x_min)/N1*i)
    y.append(y_min + (y_max-y_min)/N1*i)
Bx,By = Bdipole(x, y, M)
x1, y1 = np.meshgrid(x, y)

absB = (Bx**2 + By**2)**0.5
bx= Bx/ absB
by= By/ absB

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
quiv = ax1.quiver(y1, x1, bx, by)


fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
cont = ax2.contour(y1, x1, absB, 17)
