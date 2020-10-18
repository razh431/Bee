import numpy
import math
import csv
import bee1
from start_end import startFrame, endFrame, path
from scipy import signal

"""find instantaneous velocity of bees by averaging ____ (the parameter crop) before current frame"""

def vel(num_frames, crop):
    #crop is the average mean filter

    v = []

    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        row_num = [row for idx, row in enumerate(reader) if idx in range(0,num_frames)]

    #calculate moving mean 
    x, y = moving_mean(row_num, crop)

        #calculates instantaneous
        # instantv = inst(row_num)

    velocity = avg_vel(x, y)
    return velocity


def inst(row_num):
    #calcualtes instantaenous velocity. not using because lots of noise of xy positions. 
    velocity = []

    for x in range(0, len(row_num)):
        if x > 0 and x < len(row_num):
            distancei = numpy.array((float(row_num[x-1][12]), float(row_num[x-1][13])))
            distancef = numpy.array((float(row_num[x+1][12]), float(row_num[x+1][13])))
            #velocity is defined as distance over time, where time here is frames.
            velocity.append(numpy.linalg.norm((distancef - distancei))/2)

    return velocity

def moving_mean(row_num, crop):
    #use crop as moving mean window length
    x = []
    y = []
    #add them into the x, y positions-- creating a filtered x y positoin
    for i in range(0, len(row_num)):
        x.append(numpy.array(float(row_num[i][12])))
        y.append(numpy.array(float(row_num[i][13])))

    avgx = ret(x, n = crop)
    avgy = ret(y, n = crop)

    return avgx, avgy

def ret(x, n):
    #moving mean calculation. taken from 
    #https://stackoverflow.com/questions/14313510/how-to-calculate-moving-average-using-numpy
    ret = numpy.cumsum(x, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


def avg_vel(x, y):
    #calculate average velocity of moving mean of basically 1. 
    velocity = []
    for i in range(0, len(x)):
        if i > 0 and i < len(x)-1:
            #1 frame before, 1 frame after and average the 2
            disti = numpy.array(x[i-1], y[i-1])
            distf = numpy.array(x[i+1], y[i+1])
            velocity.append(numpy.linalg.norm((disti - distf))/2)

    return velocity
