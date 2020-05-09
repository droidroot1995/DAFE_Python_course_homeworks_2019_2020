import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

g = - 9.8
t0 = 0
dt = 0.1
v0 = 5
y0 = 20
x0 = 0
theta0 = np.pi / 6
v = [v0]
vy = [v0 * np.sin(theta0)]
vx = v0 * np.cos(theta0)
y = [y0]
x = [x0]
t = [t0]

j = 1
        
fig, ax = plt.subplots(2, 2)

def animate(i):
    global j, vx, v0, theta0

    if (y[-1] <= 0):
        #vx = 0
        #vy.append(0)
        vy.append(v[-1] * np.sin(theta0))
        vx = -vx
    else:
        vy.append(vy[-1] + g*dt)

    t.append(t[-1] + dt)
    v.append((vy[-1]**2 + vx**2)**0.5)
    y.append(y[-1] + np.sign(vy[-1])*v[i]*dt)
    x.append(x[-1] + vx*dt)

    j += 1
    ax[0][0].clear()
    ax[0][0].set_xlim(0, max(x)*(1.2) + 1 )
    ax[0][0].set_ylim(0, max(y)*(1.2) + 1 )
    ax[0][0].set_ylabel('y')
    ax[0][0].set_xlabel('x')
    ax[0][0].scatter(x[-1], y[-1])

    ax[0][1].set_xlim(0, max(t)*1.2)
    ax[0][1].set_ylim(0, max(v) + 1)
    ax[0][1].set_ylabel('v')
    ax[0][1].set_xlabel('t')
    ax[0][1].scatter(t[-1], v[-1])

    ax[1][0].set_xlim(0, max(t)*1.2)
    ax[1][0].set_ylim(vx*0.8, vx*1.2)
    ax[1][0].set_ylabel('vx')
    ax[1][0].set_xlabel('t')
    ax[1][0].scatter(t[-1], vx)

    ax[1][1].set_xlim(0, max(t) + 0.2)
    ax[1][1].set_ylim(min(vy) - 1, max(vy)*1.2)
    ax[1][1].set_ylabel('vy')
    ax[1][1].set_xlabel('t')
    ax[1][1].scatter(t[-1], vy[-1])

ani = animation.FuncAnimation(fig, animate, interval=2)
plt.show()    

    
