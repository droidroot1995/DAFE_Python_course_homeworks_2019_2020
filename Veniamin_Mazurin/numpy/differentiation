import matplotlib
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 100) 
plt.plot(x,(np.e**x)*np.sin(x) , label='exp(x)*sin(x)') 
plt.show() 

def dif(x ,x0, x1):
    a=[]
    for i in range (int((x1-x0)/0.05)):
        a.append(i*0.05)
    i=a.index(x)
    return (np.exp(a[i+1])*np.sin(a[i+1])- np.exp(a[i-1])*np.sin(a[i-1]))/0.1
        
print(dif(1,0,2))
