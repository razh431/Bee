import numpy as np
import math
import csv

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter


import bee1
import angle
import bee_info
import velocity
import airspeed

from start_end import startFrame, endFrame, path, vid_num


"""plotting velocity, antennae length, angles, orienttion angle graph vs time on same graph"""

x = [frame for frame in range(startFrame, endFrame, 1)]
# angle = [angle.ant_cba_angle_2d(i) for i in x]

#angles between body and antennas
l_angle = []
r_angle = []
orientation = []
for i in x:
    left_angle, right_angle, ori = angle.ant_cba_angle_2d(i-startFrame)
    orientation.append(ori)
    l_angle.append(left_angle)
    r_angle.append(right_angle)


#length of antennas throughout video
antl_length, antr_length = angle.ant_len(0, endFrame-startFrame)

#velocity of bees, weighted average-- second parameter is the weight. 
vel = velocity.vel(endFrame-startFrame, 50)

#other behavioral parameters, refer o their specific python files
total_angle = [antl_length[i] + antr_length[i] for i in range(len(antl_length))]
delta_tot_angle = angle.roc_angle(total_angle)
ori_angle = angle.orientation_rate(orientation)

#make them all the same length, just truncating the beginning. offset because of velocity
if len(vel) != len(x):
    crop = 50
    x = x[crop:-1]
    r_angle = r_angle[crop:-1]
    l_angle = l_angle[crop:-1]
    delta_tot_angle = angle.roc_angle(total_angle)[crop-1:]

    total_angle = total_angle[crop:-1]
    antl_length = antl_length[crop:-1]
    antr_length = antr_length[crop:-1]
    airv = airspeed.airv()[crop:-1]
    ori_angle = ori_angle[crop-1:]


#keep these subplots 3 at a time
fig, axs = plt.subplots(3)
fig.suptitle('plots: ' + str(crop) + ', bee number: ' + str(vid_num))
axs[0].plot(x, vel)
axs[0].set_title('velocity w/ avg mean of ' + str(crop))

axs[1].plot(x, airv)
axs[1].set_title('airspeed')

axs[2].plot(x, total_angle)
axs[2].set_title('total angle')


#graphing LEFT antenna length, total angle change, and orientation rate
fig1, axs1 = plt.subplots(3)
fig1.suptitle('plots: ' + str(crop) + ', bee number: ' + str(vid_num))

axs1[0].plot(x, antl_length)
axs1[0].set_title('antl_length')

axs1[1].plot(x, delta_tot_angle)
axs1[1].set_title('change in angle')

axs1[2].plot(x, ori_angle)
axs1[2].set_title('orientation')


plt.xlabel('frame number')
# plt.ylabel('y - axis'


metadata = dict(title='Bee Graphs')
writer = FFMpegWriter(fps=15, metadata=metadata)

#save vid
with writer.saving(fig, str(crop) + ', bee number: ' + str(vid_num) + ".mp4", 100):
    for i in x:
        writer.grab_frame()

plt.show()
