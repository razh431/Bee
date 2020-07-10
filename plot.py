import numpy as np
import math
import csv
import bee1

import angle
import bee_info
import antennae
import velocity

import matplotlib.pyplot as plt

"""velocity, antennae length, angles, plot on same"""

#x axis
x = [frame for frame in range(1048, 1939, 1)]
# angle = [angle.ant_cba_angle_2d(i) for i in x]

#angles between body and antennas
l_angle = []
r_angle = []
for i in x:
    left_angle, right_angle = angle.ant_cba_angle_2d(i)
    l_angle.append(left_angle)
    r_angle.append(right_angle)

#length of antennas throughout video
antl_length, antr_length = angle.ant_len()
# print(len(l_angle))
#velocity of bees
vel = velocity.vel()


# l_angle_l = plt.plot(x, l_angle)
plt.plot(x,r_angle + l_angle)
l_ant_len_l = plt.plot(x, antl_length)
plt.plot(x, antr_length)
vel_l = plt.plot(x, vel)

# plt.legend((l_angle_l, l_ant_len_l, vel_l), ('Left angle', 'Left antenna length', 'velocity'))


plt.xlabel('frame number')
plt.ylabel('y - axis')

plt.title('Graph')

plt.show()
