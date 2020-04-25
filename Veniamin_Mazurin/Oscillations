%matplotlib inline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy import integrate
import math as m
import scipy.linalg as la
import scipy.sparse.linalg as sla
 
def oscillator(t, z):
    global omega0, Omega, gamma, A0
    dy = np.zeros(2)
    dy[0] = z[1]
    dy[1] = (-1*(omega0)**2)*z[0] - gamma* z[1] - A0 * np.cos ( Omega * t)

    return dy

omega0 = 3
Omega = 2
gamma = 0.5
A0 = 1

#N = 1e4
R0 = [1.0, 0.]
t0, t1 = 0, 50*( 2*m.pi / omega0 )                # start and end
t = np.linspace(t0, t1, 10000)
R = np.zeros((len(t), len(R0)), dtype=np.float64)   # array for solution
R[0, :] = R0
r = integrate.ode(oscillator).set_integrator("dopri5")  # choice of method
r.set_initial_value(R0, t0)   # initial values
for i in range(1, t.size):
    R[i, :] = r.integrate(t[i]) # get one more value, add it to the array
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
surf2 = ax2.plot(R[:, 0], R[:,1])
