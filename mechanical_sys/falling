from numpy import linspace
import matplotlib.pyplot as plt

v0 = 5
y0 = 10
g = 9.81
t = linspace(0, 1, 1001)
m = 3

y = (y0 + v0*t + 0.5*g*t**2) * (-1)
v = v0 + g*t
g = (v - v0) / t
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

plt.plot(t, g)
plt.xlabel(u't')
plt.ylabel(u'g')
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
