import matplotlib.pyplot as plt
import numpy as np
from pylab import show

x = np.arange(0, 5, .1)
y = np.sin(x)

plt.plot(x, y)

show()
