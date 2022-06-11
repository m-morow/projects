import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('macosx')

data_name = 'Yale 2022 Substrate, 04082022'
data_array = np.loadtxt('./SUBSTRATE_ImageScan.txt', skiprows=13)
A = data_array.T
length = int(np.sqrt(len(A)))
data = np.reshape(A, (-1, length))  # Makes into matrix
labels = np.linspace(-0.5,0.5,11) # Manually change this
labels = np.round(labels,2)

# For surface plot
nx, ny = length, length
x = range(nx)
y = range(ny)

f = plt.figure()
h = f.add_subplot(111, projection='3d')

X, Y = np.meshgrid(x, y)  # `plot_surface` expects `x` and `y` data to be 2D
surf = h.plot_surface(X, Y, data, cmap=plt.cm.hsv, edgecolors='k', lw=0.6)
h.set_zlabel('counts')
h.set_ylabel('Theta')
h.set_xlabel('Phi')
h.set_xticks(range(0,length),labels,rotation=45)
h.set_yticks(range(0,length),labels,rotation=45)
f.colorbar(surf, shrink=0.5, aspect=5)
plt.title('{}'.format(data_name))
plt.show()

'''
# For 3D histogram plot

xpos = [range(matrix.shape[0])]
ypos = [range(matrix.shape[1])]
xpos, ypos = np.meshgrid(xpos, ypos)
zpos = np.zeros_like(xpos)
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
zpos = np.zeros_like(xpos)

dx = 0.5 * np.ones_like(zpos)
dy = dx.copy()
dz = matrix.flatten()

cmap = mpl.cm.get_cmap('jet') # Get desired colormap - you can change this!
max_height = np.max(dz)   # get range of colorbars so we can normalize
min_height = np.min(dz)
# scale each z to [0,1], and get their rgb values
rgba = [cmap((k-min_height)/max_height) for k in dz] 

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=rgba, zsort='average')
plt.show()
'''