#Create stereonet of strikes / dips, and poles

import numpy as np
import mplstereonet
import matplotlib.pyplot as plt
from collections import OrderedDict

strike1, dip1 = 230, 44
strike2, dip2 = 150, 70
strike3, dip3 = 330, 72
strike4, dip4 = 331, 75
strike5, dip5 = 320, 80
strike6, dip6 = 352, 24
strike7, dip7 = 350, 81
strike8, dip8 = 210, 15
strike9, dip9 = 230, 20
strike10, dip10 = 190, 23
strike11, dip11 = 210, 20
strike12, dip12 = 210, 36
strike13, dip13 = 175, 25

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='stereonet')
ax.plane(strike1, dip1, c='deepskyblue', label='Jtc %03d/%02d' % (strike1, dip1))
ax.pole(strike1, dip1, c='k')
ax.plane(strike2, dip2, c='saddlebrown', label='Jp %03d/%02d' % (strike2, dip2))
ax.pole(strike2, dip2, c='k')
ax.plane(strike3, dip3, c='saddlebrown', label='Jp %03d/%02d' % (strike3, dip3))
ax.pole(strike3, dip3, c='k')
ax.plane(strike4, dip4, c='saddlebrown', label='Jp %03d/%02d' % (strike4, dip4))
ax.pole(strike4, dip4, c='k')
ax.plane(strike5, dip5, c='orange', label='Js %03d/%02d' % (strike5, dip5))
ax.pole(strike5, dip5, c='k')
ax.plane(strike6, dip6, c='darkgreen', label='Kgl %03d/%02d' % (strike6, dip6))
ax.pole(strike6, dip6, c='k')
ax.plane(strike7, dip7, c='red', label='Kp %03d/%02d' % (strike7, dip7))
ax.pole(strike7, dip7, c='k')
ax.plane(strike8, dip8, c='red', label='Kp %03d/%02d' % (strike8, dip8))
ax.pole(strike8, dip8, c='k')
ax.plane(strike9, dip9, c='red', label='Kp %03d/%02d' % (strike9, dip9))
ax.pole(strike9, dip9, c='k')
ax.plane(strike10, dip10, c='magenta', label='Kgu %03d/%02d' % (strike10, dip10))
ax.pole(strike10, dip10, c='k')
ax.plane(strike11, dip11, c='rebeccapurple', label='Kb %03d/%02d' % (strike11, dip11))
ax.pole(strike11, dip11, c='k')
ax.plane(strike12, dip12, c='mediumseagreen', label='Ka %03d/%02d' % (strike12, dip12))
ax.pole(strike12, dip12, c='k')
ax.plane(strike13, dip13, c='mediumseagreen', label='Ka %03d/%02d' % (strike13, dip12))
ax.pole(strike13, dip13, c='k')
#ax.legend(loc=4)
ax.grid()
ax.set_title('Snake River Stereonet', y=1.10, fontsize=15)
ax.set_azimuth_ticks([])
label = np.arange(0,360,45)
labx= 0.5-0.55*np.cos(np.radians(label+90))
laby= 0.5+0.55*np.sin(np.radians(label+90))
for i in range(len(label)):
    ax.text(labx[i],laby[i],str(int(label[i]))+'\N{DEGREE SIGN}', transform=ax.transAxes, ha='center', va='center')
plt.savefig('stereonet.pdf')
plt.show()
