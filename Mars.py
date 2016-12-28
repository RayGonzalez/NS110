


#r = [1.691,1.379,1.503,1.639,1.675,1.680,1.640,1.570,1.380,1.460,1.630,1.670,1.650]

#theta = [149.22,149.22,149.22,149.22,149.22,149.60,182.50,219.70,341.00,42.50,96.30,142.30,168.60]

import pylab as plt
import numpy as np


#N = 150
r = [1.691,1.379,1.503,1.639,1.675,1.680,1.640,1.570,1.380,1.460,1.630,1.670,1.650]
theta = [149.22,149.22,149.22,149.22,149.22,149.60,182.50,219.70,341.00,42.50,96.30,142.30,168.60]
area = 20
colors = theta
ax = plt.subplot(111, polar=True)

c = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.hsv)

th_err = [0.07,0.80,0.03,0.02,0.08,5.30,1.00,1.30,4.50,2.90,0.40,0.40,1.90]
r_err = [0.002,0.011,0.001,0.001,0.002,0.100,0.040,0.040,0.005,0.080,0.010,0.290,0.040]

i=0

for th,  _r in zip(theta, r):

        local_theta = np.linspace(-th_err[i], th_err[i], 100) + th
        local_r = np.linspace(-r_err[i], r_err[i],100) + _r
        ax.plot(local_theta, local_r, color='k', marker='')

        i+=1



#c.set_alpha(0.75)

plt.show()
