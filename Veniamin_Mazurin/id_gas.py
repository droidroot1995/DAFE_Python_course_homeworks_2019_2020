import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

T=287
N=15 
m0= 14* 1.66 * 10**(-27)
k= 1.380649 * 10 ** (-23)

fig, ax = plt.subplots()

t=0
dt=0.1 
x=[random.random() for i in range(N)] 
y=[random.random() for i in range(N)]
vx=[10*random.random() for i in range(N)]
vy=[10*random.random() for i in range(N)]
'''for i in range(N):
    x.append ( random.random())
    y.append ( random. random())
    vx.append ( 10* random.random() )
    vy.append( 10* random.random() )'''

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.scatter(x, y)

print(x)
print(y)

def f(v,m,T):
    return 4* (np.pi)**(0.5) * ( m/ (2*k*T))** (1.5) *(np.e)**( -m*v**2/ (2*k*T))* v**2

def animate(i):
    global t
    t+=dt
    ax.clear()
    for i in range(N):
        x[i]+= vx[i] *dt
        y[i]+= vy[i] *dt
        if x[i]<=0:
            x[i]=0
            vx[i]*=(-1)
        if x[i] >=1:
            x[i]=1
            vx[i]*=(-1)
        if y[i]<=0:
            y[i]=0
            vy[i]*=(-1) 
        if y[i] >=1:
            y[i]=1
            vy[i]*=(-1)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.scatter(x, y)
    

        
ani = animation.FuncAnimation(fig, animate, interval=0.0001)

plt.show()
