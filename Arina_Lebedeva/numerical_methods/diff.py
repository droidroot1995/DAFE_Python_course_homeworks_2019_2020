import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import random

def fun(x):
       return x*x

def d_fun(x):
       h = 0.0000001
       return (fun(x+h)-fun(x-h))/(2*h)

x0 = float(input())
x1 = float(input())
x = random.uniform(x0, x1)
print (x)
print (d_fun(x))

x = np.arange(-10, 10, 0.2)
y = fun(x)
fig, axs = plt.subplots()
plt.axis([-10, 10, - 10, 10])
plt.scatter(x, y)
plt.show()
