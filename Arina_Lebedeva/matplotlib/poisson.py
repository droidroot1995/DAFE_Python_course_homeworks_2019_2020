import matplotlib
import numpy as np
import matplotlib.pyplot as plt

x = np.random.poisson(1.5, 1000)
mu = 1.5
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)
y = ((np.exp(-mu) * mu * x)/np.math.factorial(x))
plt.plot(bins, y, '--') 
plt.xlim(40, 160)
plt.ylim(0, 0.03)
plt.grid(True)
plt.show()
