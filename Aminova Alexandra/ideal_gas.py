import matplotlib
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 50
dt = 0.001
V = 1
T = 270
m = 6.64 * 10**(-22) 
k = 1.38 * 10**(-23)

v = (2*N*k*T/m)**0.5
vx = [(random.uniform(-1, 1))*v for i in range(N)]
vy = [(random.uniform(-1, 1))*v for i in range(N)]

x = [random.uniform(-1, 1) for i in range(N)]
y = [random.uniform(-1, 1) for i in range(N)]
fig, ax = plt.subplots()
j = 1

def animate(k):
    global j, x, y, dt, vx, vy, N

    for i in range(N):
        if x[i] >= 1 or -1 >= x[i]: 
            vx[i] *= -1
        x[i] = x[i] + vx[i]*dt
        
        if y[i] >= 1 or -1 >= y[i]: 
            vy[i] *= -1
        y[i] = y[i] + vy[i]*dt

    j += 1

    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_title('Ideal gas')
    ax.scatter(x, y)
    
ani = animation.FuncAnimation(fig, animate, interval=2)
plt.show()
