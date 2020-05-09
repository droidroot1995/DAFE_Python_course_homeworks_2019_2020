import matplotlib
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N1 = 50
N2 = 30
dt = 0.001

T = 270
m1 = 9.64 * 10**(-22)
m2 = 7.2 * 10**(-21)
k = 1.38 * 10**(-23)

v1 = (2*N1*k*T/m1)**0.5
v2 = (2*N2*k*T/m2)**0.5

vx1 = [(random.uniform(-1, 1))*v1 for i in range(N1)]
vx2 = [(random.uniform(-1, 1))*v2 for i in range(N2)]

vy1 = [(random.uniform(-1, 1))*v1 for i in range(N1)]
vy2 = [(random.uniform(-1, 1))*v2 for i in range(N2)]

x1 = [random.uniform(-1, 1) for i in range(N1)]
y1 = [random.uniform(-1, 1) for i in range(N1)]
x2 = [random.uniform(-1, 1) for i in range(N2)]
y2 = [random.uniform(-1, 1) for i in range(N2)]

fig, ax = plt.subplots()
j = 1

def animate(k):
    global j, dt, x, y, vx, vy, N1, N2

    for i in range(N1):
        if x1[i] >= 1 or -1 >= x1[i]: 
            vx1[i] *= -1
        x1[i] += vx1[i]*dt
        
        if y1[i] >= 1 or -1 >= y1[i]: 
            vy1[i] *= -1
        y1[i] += vy1[i]

    for i in range(N2):
        if x2[i] >= 1 or -1 >= x2[i]: 
            vx2[i] *= -1
        x2[i] += vx2[i]*dt
        
        if y2[i] >= 1 or -1 >= y2[i]: 
            vy2[i] *= -1
        y2[i] += vy2[i]
        
    j += 1

    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_title('Ideal gases')
    ax.scatter(x1, y1, color = "#FF00FF")
    ax.scatter(x2, y2, color = "#0000FF")
    
ani = animation.FuncAnimation(fig, animate, interval=2)
plt.show()
