import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import random

def fun(x):
       return np.exp(x)*np.sin(x)

def d_fun(x):
       h = 0.0000001
       return (fun(x+h)-fun(x-h))/(2*h)

x0 = 0
x1 = 1
x = random.uniform(x0, x1)
print (x)
print (d_fun(x))

x = np.arange(-10, 10, 0.002)
y = fun(x)
fig, axs = plt.subplots()
plt.axis([-10, 10, - 10, 10])
plt.scatter(x, y)
plt.show()
