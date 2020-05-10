import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import random
x = np.random.poisson(1.5, 1000)
n,bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)
y = ((np.exp(-1.5))*1.5*x)/(np.math.factorial(x))
plt.plot(y, '--')  
plt.title('Poisson')
plt.text(60, .025, r'$\lambda=1.5')
plt.xlim(0, 100)
plt.ylim(-2, 20)
plt.grid(True)
plt.show()
