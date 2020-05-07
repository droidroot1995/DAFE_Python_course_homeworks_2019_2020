import numpy as np
def difeq(t0,y0,t1,n):
    y=[]
    h = (t1-t0)/n
    y.append(y0)
    for i in range(1, n+1):
        y.append(y[i-1]+ h*(t0+ i*h )*np.sqrt(y[i-1]))
    return y
                 
a=difeq(0,1,1,10)
print(a)
