import numpy as np
import math
import csv
import bee1

import angle
import bee_info
import velocity
import single
import matplotlib.pyplot as plt

from start_end import startFrame
from start_end import endFrame
#x axis

"""velocity, antennae length, angles, plot on same"""

x = [frame for frame in range(startFrame, endFrame, 1)]
# angle = [angle.ant_cba_angle_2d(i) for i in x]

#angles between body and antennas
l_angle = []
r_angle = []
for i in x:
    left_angle, right_angle = angle.ant_cba_angle_2d(i-startFrame)
    l_angle.append(left_angle)
    r_angle.append(right_angle)

#length of antennas throughout video
antl_length, antr_length = angle.ant_len(0, endFrame-startFrame)
if len(antl_length) == len(antr_length):
    print('please make this work')
#velocity of bees
vel = velocity.vel(endFrame-startFrame)
total_angle = [antl_length[i] + antr_length[i] for i in range(len(antl_length))]


if len(vel) != len(x):
    x = x[1:-1]
    r_angle = r_angle[1:-1]
    l_angle = l_angle[1:-1]
    total_angle = total_angle[1:-1]
    antl_length = antl_length[1:-1]
    antr_length = antr_length[1:-1]


plt.plot(x, total_angle)
plt.plot(x, antr_length)
plt.plot(x, antl_length)
vel_l = plt.plot(x, vel)



plt.xlabel('frame number')
plt.ylabel('y - axis')

plt.title('Graph')

plt.show()
