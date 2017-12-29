import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure()  # create a figure
ax = fig.gca(projection='3d')  # create a 3-dim axis
X = np.arange(-5, 5, .25)  # horizontal range
Y = np.arange(-5, 5, .25)  # vertical range
X, Y = np.meshgrid(X, Y)  # create a special grid
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)

surf = ax.plot_surface(
    X, Y, Z,
    rstride=1, cstride=1,
    cmap=cm.coolwarm,
    linewidth=0,
    antialiased=False
)
ax.set_zlim(-1.01, 1.01)  # z-axis

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(
    surf,
    shrink=0.5,
    aspect=5
)

plt.show()  # display the figure
