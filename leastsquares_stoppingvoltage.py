import numpy as np
import matplotlib.pyplot as plt
from scipy import special
from scipy.optimize import curve_fit
import scipy.optimize as opt
import scipy.constants as constant
import math as math
from matplotlib import rcParams
plt.style.use('default')
rcParams['figure.dpi'] = 150
import pandas as pd 

data = pd.read_csv("lab3_purp.csv",skipinitialspace=True,sep=",")
x = data405_purp[:,0]
y = data405_purp[:,1]/100

def func(x,a,b,c,vs):
    return (a * (vs-x)**3 * np.heaviside(vs-x,1) + b * (vs-x)**4 * np.heaviside(vs-x,1)) / (1 + c * (vs-x)**2 * np.heaviside(vs-x,1))

popt, pcov_purp = curve_fit(func,x,y,bounds=([-100,-100,-100,1],[100,100,100,2]),method='trf')
print("vs = {:8.5f}".format(popt[3]))
print(popt)

fig=plt.figure()
ax = fig.add_subplot(111)

plt.scatter(data405_purp[:,0],data405_purp[:,1]/100,c='#9467bd') #s=10 for size
plt.plot(x[5:15],(func(x,*popt)[5:15]),c='black')
#work in mAmps

plt.title('Current vs retarding voltage, \u03BB=405 nm')
ax.set_xlabel('retarding potential (volts)')
ax.set_ylabel('photodiode current (mAmps)')

bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
ax.text(2.1, 0.405, "vs = 1.41044 V", ha="center", va="center", size=11,
        bbox=bbox_props)

plt.show()
