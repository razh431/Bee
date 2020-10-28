from start_end import startFrame, endFrame, path, vid_num

# import new_mapping
import plot
import os
from multiprocessing import Process

import numpy as np
import matplotlib
import cv2
# matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter

# Set up video writer
metadata = dict(title='Bee Animation', artist='Matplotlib',
                comment='This data is ... ')
writer = FFMpegWriter(fps=15, metadata=metadata)

# Get Video
vidObj = cv2.VideoCapture('/Users/rachelzhou/Research/build_opencv/opencv/samples/python/single/bee6.avi')

vidObj.set(1, 50)

ret, frame = vidObj.read()



sec = []
for x in plot.x:
    x = x/23.39
    sec.append(x)

t = np.array(sec)
x = np.array(plot.get_data(5))
y = np.array(plot.get_data(0))
z = np.array(plot.get_data(3))



# Configure subplots
fig, axs = plt.subplots(3, 2, sharex='col')

# Initialize the line plots
axs[0, 0].plot(t, x)
axs[0, 0].set_ylabel('velocity' + '\n' + '(pixels per second)')


axs[1, 0].plot(t, y)
axs[1, 0].set_ylabel('angle between' + '\n' + ' antennae (degrees)')


axs[2, 0].plot(t, z)
axs[2, 0].set_ylabel('airflow (meters' + '\n' + ' per second)')
plt.sca(axs[2, 0])
plt.yticks(np.arange(0, 5.5, 0.5))


axs[0, 0].xaxis.set_visible(False)
axs[1, 0].xaxis.set_visible(False)


# Initialize the dots
x_dot, = axs[0, 0].plot(t[0], x[0], 'ro')
plt.ylabel('velocity')
y_dot, = axs[1, 0].plot(t[0], y[0], 'ro')
plt.ylabel('total angle')
z_dot, = axs[2, 0].plot(t[0], z[0], 'ro')
plt.ylabel('airflow (meters' + '\n' + ' per second)')
plt.xlabel('time in seconds')

# Initialize first frame
im = axs[0, 1].imshow(frame)

# Remove unused subplots
axs[1, 1].axis('off')
axs[2, 1].axis('off')


# In a loop, plot the ith value of x, y and z as a travelling dot and update the video frame
with writer.saving(fig, "bee6_data2.mp4", 23):
    for t_i, x_i, y_i, z_i in zip(t, x, y, z):
        x_dot.set_data([t_i, x_i])
        y_dot.set_data([t_i, y_i])
        z_dot.set_data([t_i, z_i])
        ret, frame = vidObj.read()
        im.set_data(frame)
        plt.pause(0.01)  # remove pause and uncomment matplotlib.use("Agg") to make it faster
        writer.grab_frame()
