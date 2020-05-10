import numpy as np
import matplotlib.pyplot as plt


v0 = 5
y0 = 10
g = 9.81
t = linspace(0.0000001, 1, 1001)
m = 3
a = np.pi / 3
x0 = 0

x = x0 + (v0 * np.cos(a)) / t
y = y0 + v0*t*np.sin(a) - 0.5*g*t*t
v = np.sqrt(v0*v0*np.cos(a)*np.cos(a) * (v0*np.sin(a)- g*t)**2)
Ep = m*g*y
Ek = m*v*v*0.5
T = Ep + Ek


plt.plot(t, y)
plt.xlabel(u't')
plt.ylabel(u'y')
plt.show()

plt.plot(t, v)
plt.xlabel(u't')
plt.ylabel(u'v')
plt.show()


plt.plot(t, Ep)
plt.xlabel(u't')
plt.ylabel(u'Ep')
plt.show()

plt.plot(t, Ek)
plt.xlabel(u't')
plt.ylabel(u'Ek')
plt.show()

plt.plot(t, T)
plt.xlabel(u't')
plt.ylabel(u'T')
plt.show()
