import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

g = -9.8
t0 = 0
dt = 0.1
v0 = 0
y0 = 20
v = [v0]
y = [y0]
Ek = [(v0**2)/2]
t = [t0]
j = 1
fig, ax = plt.subplots(2,  2)

ax[0][0].clear()
ax[0][0].set_xlim(-1, 1)
ax[0][0].set_ylim(-15, 25)

ax[0][0].scatter(0, y[-1])


def animate(i):
    global j

    if(y[-1] <= 0):
        v.append(0)
    else:
        v.append(v[j - 1] + g*dt)
        
    t.append(t[j-1] + dt)
    y.append(y[j - 1] + v[-1]*dt)
    Ek.append(0.5*(v[-1]**2))
    
    j += 1
    ax[0][0].clear()
    ax[0][0].set_xlim(-1, 1)
    ax[0][0].set_ylim(min(y), max(y) + 1)
    ax[0][0].set_ylabel('y')
    ax[0][0].set_xlabel('x')
    ax[0][0].scatter(0, y[-1])

    ax[0][1].set_xlim(0, max(t) + 10)
    ax[0][1].set_ylim(min(y) + 1, 0)
    ax[0][1].set_ylabel('y')
    ax[0][1].set_xlabel('t')
    ax[0][1].scatter(t[-1], y[-1])

    ax[1][0].set_xlim(0, max(t) + 10)
    ax[1][0].set_ylim(0, max(Ek) + 100)
    ax[1][0].set_ylabel('Ek')
    ax[1][0].set_xlabel('t')
    ax[1][0].scatter(t[-1], Ek[-1])

    ax[1][1].set_xlim(0, max(t) + 0.2)
    ax[1][1].set_ylim(min(v) - 1, 1)
    ax[1][1].set_ylabel('v')
    ax[1][1].set_xlabel('t')
    ax[1][1].scatter(t[-1], v[-1])

ani = animation.FuncAnimation(fig, animate, interval=2)
plt.show()
