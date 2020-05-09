%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
def fall(x0,y0,g,v0,n,dt,k):
    t0 = 0
    y=[y0]
    v_y=[v0 * np.sin(k)]
    x=[x0]
    t=[t0]
    
    for i in range(1, n):
        t.append(t[i-1] + dt)
        v_y.append (v_y[i-1] + g*dt)
        y.append (y[i-1] + dt*v_y[i-1])
        x.append( x[i-1] + v0* np.cos(k)*dt )
    
    return (t, x, y, v_y)

t, x, y, v_y = fall(0, 10, -9.8, 10,100, 0.01, 0.765 )

plt.plot(t, y)
plt.plot( x , y )
plt.show()
