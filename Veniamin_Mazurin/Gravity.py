import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

v0 =10
x0=0
th = 0.765
h = 10
dt = 0.1
t0 = 0
a = -9.8
y=[h]
v_y=[v0* np.sin(th)]
v=[v0]
t=[t0]
e_k = [v0**2/2]
e_p= [-a * h ]
x=[x0]

fig, ax = plt.subplots(3, 2)

j = 1

ax[0][0].clear()
ax[0][0].set_xlim(x0,max(x)+3 )
ax[0][0].set_ylim(0, max(y)+3)
ax[0][0].scatter(0, h)

ax[0][1].clear()
ax[0][1].set_xlim(t0, max(t) + 1)
ax[0][1].set_ylim(0, max(y) + 1)
ax[0][1].set_xlabel('t')
ax[0][1].set_ylabel('y(t)')
ax[0][1].plot(t0, h)

ax[1][0].clear()
ax[1][0].set_xlim(t0, max(t) + 1)
ax[1][0].set_ylim(min(v) - 1 , max(v) + 1)
ax[1][0].set_xlabel('t')
ax[1][0].set_ylabel('v(t)')
ax[1][0].plot(t0, v0 )

ax[1][1].clear()
ax[1][1].set_xlim(t0, max(t) + 1)
ax[1][1].set_ylim( 0 , max(v) + 1)
ax[1][1].set_xlabel('t')
ax[1][1].set_ylabel('e_k(t)')
ax[1][1].plot(t, e_k)

ax[2][1].clear()
ax[2][1].set_xlim(t0, max(t) + 1)
ax[2][1].set_ylim( 0 , max(v) + 1)
ax[2][1].set_xlabel('t')
ax[2][1].set_ylabel('e_p(t)')
ax[2][1].plot(t, e_p)





def animate(i):
    global j


    t_j = t[j-1] + dt
    v_y_j = v_y[j-1] + a*dt
    y_j = y[j-1] + 0.5*(v_y[j-1] + v_y_j)*dt
    x_j= x[j-1] + v0* np.cos(th) * dt

    if y_j <=0:
        v_y_j = -v_y_j
        y_j = 0

    e_k_j = (v_y_j**2 + (v0 * np.cos( th))**2) / 2
    e_p_j = -a * y_j
    t.append(t_j)
    v_y.append(v_y_j) #
    v.append((v_y_j**2+ (v0* np.cos(th))**2)**(1/2) )
    y.append(y_j)
    x.append(x_j)
    e_k.append(e_k_j)
    e_p.append(e_p_j)

    j += 1

    ax[0][0].clear()
    ax[0][0].set_xlim(x0, max(x) +3)
    ax[0][0].set_ylim(0, max(y) +3 )
    ax[0][0].scatter(x[-1], y[-1])

    ax[0][1].clear()
    ax[0][1].set_xlim(t0, max(t) + 3)
    ax[0][1].set_ylim(0, max(y) + 3)
    ax[0][1].set_xlabel('t')
    ax[0][1].set_ylabel('y(t)')
    ax[0][1].plot(t, y)

    ax[1][0].clear()
    ax[1][0].set_xlim(t0, max(t) + 5)
    ax[1][0].set_ylim(min(v) - 2 , max(v) + 5)
    ax[1][0].set_xlabel('t')
    ax[1][0].set_ylabel('v(t)')
    ax[1][0].plot(t, v)

    ax[1][1].clear()
    ax[1][1].set_xlim(t0, max(t) + 1)
    ax[1][1].set_ylim( 0 , max(e_k) + 1)
    ax[1][1].set_xlabel('t')
    ax[1][1].set_ylabel('e_k(t)')
    ax[1][1].plot(t, e_k)

    ax[2][1].clear()
    ax[2][1].set_xlim(t0, max(t) + 1)
    ax[2][1].set_ylim( 0 , max(e_p) + 1)
    ax[2][1].set_xlabel('t')
    ax[2][1].set_ylabel('e_p(t)')
    ax[2][1].plot(t, e_p)




'''def fall(h,a,v0,n,dt):
    t0 = 0
    y=[]
    v=[]
    t=[t0]
    y.append(h)
    v.append(v0)
    
    for i in range(1, n):
        t.append(t[i-1] + dt)
        v.append (v[i-1] + a*dt)
        y.append (y[i-1] + dt*v[i-1])
    
    return (t, y, v)

t, y, v = fall(10, -9.8, 0,100, 0.01 )

plt.plot(t, y)'''

ani = animation.FuncAnimation(fig, animate, interval=0.05)

plt.show()
        
