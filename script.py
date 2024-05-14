import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# Get the input of xInitial and xFinal values from the user
xInitial = float(input("Enter the value of xInitial: "))
xFinal = float(input("Enter the value of xFinal: "))
separation = float(input("Enter the value of separation: "))

# Create the x, y, and z coordinate arrays
x = np.arange(xInitial, xFinal, separation)
y = np.arange(0, 6.2, 0.2)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)

# Create a 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)

plt.show()