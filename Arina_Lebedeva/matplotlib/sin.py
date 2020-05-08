import matplotlib
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.2)
y = np.sin(x)
fig, axs = plt.subplots()
plt.axis([0, 12, -1.5, 1.5])
plt.scatter(x, y)
plt.show()
