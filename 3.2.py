import numpy as np
import matplotlib.pyplot as plt

R = [0.6,1.1,1.9,2.6,3.4,4.3,4.8,5.9,8.5,9.5,11.2]
S = [12.4,21.9,37.9,53.1,68.0,82.3,85.7,89.5,95.2,97.5,101.1]
SErr = [8.6,6.2,6.2,9.5,6.2,6.2,6.3,15.6,15.5,6.2,10.2]
RErr = [0,0,0,0,0,0,0,0,0,0,0]


plt.errorbar(R, S, SErr, RErr, capsize=3, ls='none', color='black',
            elinewidth=1)
plt.title("Speed of objects vs Radius")
plt.show()




