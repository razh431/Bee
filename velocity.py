import numpy
import math
import csv
import bee1
from start_end import startFrame, endFrame, path
from scipy import signal

"""find instantaneous velocity of bees by averaging 1 frame after with 1 frame before current frame"""

def vel(num_frames, crop):
    #crop is the average mean filter

    v = []

    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        row_num = [row for idx, row in enumerate(reader) if idx in range(0,num_frames)]

    x, y = moving_mean(row_num, crop)

        #calculates instantaneous
        # instantv = inst(row_num)

    velocity = avg_vel(x, y)
    return velocity


def inst(row_num):
    velocity = []

    for x in range(0, len(row_num)):
        if x > 0 and x < len(row_num):
            distancei = numpy.array((float(row_num[x-1][12]), float(row_num[x-1][13])))
            distancef = numpy.array((float(row_num[x+1][12]), float(row_num[x+1][13])))
            #velocity is defined as distance over time, where time here is frames.
            velocity.append(numpy.linalg.norm((distancef - distancei))/2)

    return velocity

def moving_mean(row_num, crop):
    x = []
    y = []
    for i in range(0, len(row_num)):
        x.append(numpy.array(float(row_num[i][12])))
        y.append(numpy.array(float(row_num[i][13])))

    avgx = ret(x, n = crop)
    avgy = ret(y, n = crop)

    return avgx, avgy

def ret(x, n):
    ret = numpy.cumsum(x, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


def avg_vel(x, y):
    velocity = []
    for i in range(0, len(x)):
        if i > 0 and i < len(x)-1:
            disti = numpy.array(x[i-1], y[i-1])
            distf = numpy.array(x[i+1], y[i+1])
            velocity.append(numpy.linalg.norm((disti - distf))/2)

    return velocity
