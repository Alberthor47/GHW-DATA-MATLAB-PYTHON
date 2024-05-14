import numpy as np
import matlab.engine
import matplotlib.pyplot as plt

eng = matlab.engine.start_matlab()
# initila | final | space
args = eng.createMesh(0.0,6.0,0.001,nargout=3)
X = np.array(args[0])
Y = np.array(args[1])
Z = np.array(args[2])

print('X = ', X)
print('Y = ', Y)
print('Z = ', Z)

# Create a 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)

plt.show()

