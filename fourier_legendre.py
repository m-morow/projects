# Calculate Fourier-Legendre ak coefficients for n = 0-20
# Plot Fourier-Legendre series for
# f(x) = 0 -1<0<1
# f(x) = x 0<x<1

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import legendre
import scipy.integrate as integrate
from numpy import polynomial

# Initial conditions ----------------------------------
n = np.arange(0,21,1)
x = np.arange(-1, 1, 0.01)

# F(x) data
xs = np.array([-1,0,0.5,1])
ys = np.array([0,0,0.5,1])

# Define Legendre polynomial function -----------------
def _L(x,n):
    leg = legendre(n)
    P_n = leg(x)
    return P_n

# Finding ak coefficients -----------------------------
vals = []

for i in n:
    f = lambda x: x*_L(x,i)
    nn = (((2*i) + 1)/2)
    val = (nn*integrate.quad(f,0,1)[0])
    vals = np.append(vals,val)

# Begin of series calculations -------------------------
yy = []
yy2 = []
yy3 = []
yy6 = []
yy9 = []
yy20 = []

for i in x:
    y = np.sum(((1/4)*_L(i,0)))
    yy = np.append(yy,y)

    y2 = np.sum(((0.25)*_L(i,0))+((1/2)*_L(i,1)))
    yy2 = np.append(yy2,y2)

    y3 = np.sum(((0.25)*_L(i,0))+((1/2)*_L(i,1))+((5/16)*_L(i,2)))
    yy3 = np.append(yy3,y3)

    y6 = np.sum(((0.25)*_L(i,0))+((1/2)*_L(i,1))+((5/16)*_L(i,2))-((3/32)*_L(i,4))+(vals[6]*_L(i,5))
                +((13/256)*_L(i,6)))
    yy6 = np.append(yy6,y6)

    y9 = np.sum(((0.25)*_L(i,0))+((1/2)*_L(i,1))+((5/16)*_L(i,2))-((3/32)*_L(i,4))
                +(vals[6]*_L(i,5))+((13/256)*_L(i,6))+(vals[8]*_L(i,7))+(vals[9]*_L(i,8))
                +(vals[10]*_L(i,9)))
    yy9 = np.append(yy9,y9)

    y20 = np.sum(((0.25)*_L(i,0))+((1/2)*_L(i,1))+((5/16)*_L(i,2))-((3/32)*_L(i,4))
                +(vals[6]*_L(i,5))+((13/256)*_L(i,6))+(vals[8]*_L(i,7))+(vals[9]*_L(i,8))
                +(vals[10]*_L(i,9))+(vals[11]*_L(i,10))+(vals[12]*_L(i,11))+(vals[13]*_L(i,12))
                +(vals[14]*_L(i,13))+(vals[15]*_L(i,14))+(vals[16]*_L(i,15))+(vals[17]*_L(i,16))
                +(vals[18]*_L(i,17))+(vals[19]*_L(i,18))+(vals[20]*_L(i,19)))
    yy20 = np.append(yy20,y20)

# Plotting ---------------------------------------
fig = plt.figure()
grid = plt.GridSpec(9, 6, hspace=0.2, wspace=0.2)
ax0 = fig.add_subplot(grid[0:3, 0:3])
ax1 = fig.add_subplot(grid[3:6, 0:3])
ax2 = fig.add_subplot(grid[6:9, 0:3])
ax3 = fig.add_subplot(grid[0:3, 3:6])
ax4 = fig.add_subplot(grid[3:6, 3:6])
ax5 = fig.add_subplot(grid[6:9, 3:6])

ax0.plot(xs,ys,c='black')
ax1.plot(xs,ys,c='black')
ax2.plot(xs,ys,c='black')
ax3.plot(xs,ys,c='black')
ax4.plot(xs,ys,c='black')
ax5.plot(xs,ys,c='black')

ax0.plot(x,yy,c='r')
ax0.set_xticks([])
ax1.plot(x,yy2,c='r')
ax1.set_xticks([])
ax2.plot(x,yy3,c='r')
ax3.plot(x,yy6,c='r')
ax3.set_xticks([])
ax3.yaxis.tick_right()
ax4.plot(x,yy9,c='r')
ax4.set_xticks([])
ax4.yaxis.tick_right()
ax5.plot(x,yy20,c='r')
ax5.yaxis.tick_right()
plt.suptitle('Fourier-Legendre series of f(x) for different n values')
plt.savefig('./FL_series_p1.pdf')
plt.show()




