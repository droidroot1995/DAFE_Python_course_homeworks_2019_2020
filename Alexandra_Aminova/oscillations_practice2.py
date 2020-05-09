%matplotlib inline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import integrate
import math as m
import scipy.linalg as la
import scipy.sparse.linalg as sla

''' Создайте функцю, стоящей в правой части системы дифференциальных уравнений,
    эквивалентной уравнению (23).
    Проведите расчеты и постройте зависимости для колебательной системы с параметрами'''

def oscillator1(t, z):
    global omega0, gamma
    dy = np.zeros(2)
    
    dy[0] = z[1]
    dy[1] = -1*gamma*z[1] - ((omega0)**2)*z[0]
    
    return dy

omega0 = 3
gamma = 0.5
l = 5
g = 10
T = 2*m.pi*m.sqrt(l/g)
t0, t1 = 0, 5*T

R0 = [1., 0.]

t = np.linspace(t0, t1, 10000)
R = np.zeros((len(t), len(R0)), dtype=np.float64)   
R[0, :] = R0
r = integrate.ode(oscillator1).set_integrator("dopri5")  
r.set_initial_value(R0, t0)   
for i in range(1, t.size):
    R[i, :] = r.integrate(t[i]) 
    if not r.successful():
        raise RuntimeError("Could not integrate")

fig = plt.figure()
ax = fig.add_subplot(111)
surf = ax.plot(t, R[:,0])

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
surf1 = ax1.plot(t, R[:,1])

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
surf2 = ax2.plot(R[:,0], R[:,1])
