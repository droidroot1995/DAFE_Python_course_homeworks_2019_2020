import matplotlib
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 10, 0.2)
y = np.sin(x)
fig, ax = plt.subplots()
plt.scatter(x, y)
plt.show()
