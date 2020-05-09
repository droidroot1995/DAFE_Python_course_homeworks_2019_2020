%matplotlib inline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import integrate
import math as m
import scipy.linalg as la
import scipy.sparse.linalg as sla

''' Вычислите полную энергию гармонического осциллятора для тех моментов времени,
    в которые известны значения координаты и скорости.
    Постройте график временной зависимости величины'''

def oscillator(t, z):
    global omega
    dy = np.zeros(2)
    dy[0] = z[1]
    dy[1] = (-1*(omega)**2)*z[0]
    
    return dy

k = 9
_m = 1
T = 2*m.pi*m.sqrt(_m/k)
omega = 2*m.pi/T
N = 1e4
R0 = [0.5, 1.]

t0, t1 = 0, 5*T                

t = np.linspace(t0, t1, 10000)
R = np.zeros((len(t), len(R0)), dtype=np.float64)   
R[0, :] = R0
r = integrate.ode(oscillator).set_integrator("dopri5")  
r.set_initial_value(R0, t0)   
for i in range(1, t.size):
    R[i, :] = r.integrate(t[i]) 
    if not r.successful():
        raise RuntimeError("Could not integrate")

E = np.zeros((len(t), len(R0)), dtype = np.float64)
delta = np.zeros(len(t), dtype = np.float64)

for i in range (len(t)):
    E[i,:] = (0.5*(k*R[i,0]**2 + _m*R[i,1]**2), 0.5*k*R[i,0]**2 )
    delta[i]  = (E[i,1] - E[i,0])/E[i,0]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Delta_n')
surf = ax.scatter(t, delta, linewidth = 0.5)



