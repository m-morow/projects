import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

xs = np.array([-1,0,0.5,1])
ys = np.array([0,0,0.5,1])
x = np.arange(-1, 1, 0.01)

def _func_cos(n,x):
    return np.sum((((np.pi*n*np.sin(np.pi*n))+(np.cos(np.pi*n))-1)/(np.pi**2 * n**2))*(np.cos(np.pi*n*x)))

def _func_sin(n,x):
    return np.sum((1/(np.pi*n))*(-np.cos(np.pi*n)+(np.sin(np.pi*n)/(np.pi*n)))*(np.sin(np.pi*n*x)))

vals = []
vals2 = []
vals3 = []
vals6 = []
vals91 = []
vals92 = []
vals203 = []
vals202 = []
vals201 = []

for i in x:
    v = 0.25 + _func_cos(1,i) + _func_sin(1,i)
    vals = np.append(vals,v)

for i in x:
    v = 0.25 + _func_cos(1,i) + _func_sin(1,i) + _func_cos(2,i) + _func_sin(2,i)
    vals2 = np.append(vals2,v)

for i in x:
    v = 0.25 + _func_cos(1,i) + _func_sin(1,i) + _func_cos(2,i) + _func_sin(2,i) + _func_cos(3,i) + _func_sin(3,i)
    vals3 = np.append(vals3,v)

for i in x:
    v = np.sum(_func_cos(1,i) + _func_sin(1,i) + _func_cos(2,i) + _func_sin(2,i) + _func_cos(3,i) + _func_sin(3,i)
    + _func_cos(4, i) + _func_sin(4, i) + _func_cos(5, i) + _func_sin(5, i) + _func_cos(6, i) + _func_sin(6, i))
    vals91 = np.append(vals91,v)

for i in x:
    v = np.sum(_func_cos(7, i) + _func_sin(7, i) + _func_cos(8, i) + _func_sin(8, i) + _func_cos(9, i) + _func_sin(9, i))
    vals92 = np.append(vals92,v)

for i in x:
    v = 0.25 + _func_cos(1,i) + _func_sin(1,i) + _func_cos(2,i) + _func_sin(2,i) + _func_cos(3,i) + _func_sin(3,i)
    + _func_cos(4, i) + _func_sin(4, i) + _func_cos(5, i) + _func_sin(5, i) + _func_cos(6, i) + _func_sin(6, i)
    vals6 = np.append(vals6,v)

for i in x:
    v = np.sum(_func_cos(1,i) + _func_sin(1,i) + _func_cos(2,i) + _func_sin(2,i) + _func_cos(3,i) + _func_sin(3,i)
    + _func_cos(4, i) + _func_sin(4, i) + _func_cos(5, i) + _func_sin(5, i) + _func_cos(6, i) + _func_sin(6, i)
    + _func_cos(7, i) + _func_sin(7, i) + _func_cos(8, i) + _func_sin(8, i) + _func_cos(9, i) + _func_sin(9, i))
    vals201 = np.append(vals201, v)

for i in x:
    v = np.sum(_func_cos(10, i) + _func_sin(10, i) + _func_cos(11, i) + _func_sin(11, i) + _func_cos(12, i) + _func_sin(12, i)
    + _func_cos(13, i) + _func_sin(13, i) + _func_cos(14, i) + _func_sin(14, i) + _func_cos(15, i) + _func_sin(15, i))
    vals202 = np.append(vals202, v)

for i in x:
    v = np.sum(_func_cos(16, i) + _func_sin(16, i) + _func_cos(17, i) + _func_sin(17, i) + _func_cos(18, i) + _func_sin(18, i)
    + _func_cos(19, i) + _func_sin(19, i) + _func_cos(20, i) + _func_sin(20, i))
    vals203 = np.append(vals203,v)

vals20_final = vals201 + vals202 + vals203 + 0.25
vals9_final = vals91 + vals92

fig = plt.figure()
grid = plt.GridSpec(9, 6, hspace=0.2, wspace=0.2)
ax0 = fig.add_subplot(grid[0:3, 0:3])
ax1 = fig.add_subplot(grid[3:6, 0:3])
ax2 = fig.add_subplot(grid[6:9, 0:3])
ax3 = fig.add_subplot(grid[0:3, 3:6])
ax4 = fig.add_subplot(grid[3:6, 3:6]) 
ax5 = fig.add_subplot(grid[6:9, 3:6])

ax0.plot(x,vals,c='r',label='n=1')
ax0.set_xticks([])
ax1.plot(x,vals2,c='r',label='n=2')
ax1.set_xticks([])
ax2.plot(x,vals3,c='r',label='n=3')
ax3.plot(x,vals6,c='r',label='n=6')
ax3.set_xticks([])
ax3.yaxis.tick_right()
ax4.plot(x,vals9_final+0.25,c='r',label='n=9')
ax4.set_xticks([])
ax4.yaxis.tick_right()
ax5.plot(x,vals20_final,c='r',label='n=20')
ax5.yaxis.tick_right()
ax0.plot(xs,ys,c='k')
ax1.plot(xs,ys,c='k')
ax2.plot(xs,ys,c='k')
ax3.plot(xs,ys,c='k')
ax4.plot(xs,ys,c='k')
ax5.plot(xs,ys,c='k')
ax0.legend()
ax1.legend()
ax2.legend()
ax3.legend()
ax4.legend()
ax5.legend()
plt.suptitle('Fourier series of f(x) for different n values')
plt.savefig('./fourier_series_p1.pdf')
plt.show()
