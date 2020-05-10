import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import random
import math
x = np.random.poisson(1.5, 1000)
n,bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)

def myfunction(x):
  return np.math.factorial(x)

myfunction2 = np.vectorize(myfunction)

y = ((np.exp(-1.5))*1.5*x)/(myfunction2(x))
plt.plot(y, '--')  
plt.title('Poisson')
plt.text(60, .025, r'$\lambda=1.5')
plt.xlim(0, 100)
plt.ylim(-2, 20)
plt.grid(True)
plt.show()
