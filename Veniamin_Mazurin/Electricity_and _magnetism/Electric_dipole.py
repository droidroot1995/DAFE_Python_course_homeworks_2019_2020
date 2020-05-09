%matplotlib inline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import integrate
import math as m

def phi(q, xq, yq, X, Y):
    e0 = 8.85e-12
    Nq = len(q)
    Nx = len(X)
    Ny = len(Y)
    
    M = np.zeros((Nx, Ny))
    
    for i in range(Nx):
        for j in range(Ny):
            s = 0
            for k in range(Nq):
                s = s + q[k]/((X[i] - xq[k])**2+(Y[j] - yq[k])**2)**0.5
            
            M[i, j] = s/(4*e0*m.pi)
    return M
e=1.6e-16
R_0 = 1e-10
q = [-e, e]
xq = [-R_0, R_0]

yq = np.zeros(2)

N1 = 50
x_min = -2*R_0
y_min = -2*R_0

x_max = 2*R_0
y_max = 2*R_0

x = []
y = []
for i in range(N1):
    x.append(x_min+(x_max-x_min)/N1*i)
    y.append(y_min + (y_max-y_min)/N1*i)
    
M = phi(q, xq, yq, x, y)
x1, y1 = np.meshgrid(x, y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(y1, x1, M, linewidth=0)


fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
cont = ax2.contour(y1, x1, M, 33)

px, py = np.gradient(-M, 0.1, 0.1)

px1 = px/((px**2 + py**2)**0.5)
py1 = py/((px**2 + py**2)**0.5)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
quiv = ax1.quiver(y1, x1, px1, py1, 0.5)

mp = (px**2 + py**2)**0.5

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
cont = ax2.contour(y1, x1, mp, 17)

