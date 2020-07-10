import numpy
import math
import csv
import bee1

"""find instantaneous velocity of bees by averaging 1 frame after with 1 frame before current frame"""

def vel(num_frames):

    v = []

    with open("bee3_modified.csv") as csvfile:
        reader = csv.reader(csvfile)

        row_num =[row for idx, row in enumerate(reader) if idx in range(0,num_frames)]

        velocity = []

        #calculates
        for x in range(0, len(row_num)):
            petiole = numpy.array((float(row_num[x][12]), float(row_num[x][13])))

            if x > 0 and x < len(row_num)-1:
                distancei = numpy.array((float(row_num[x-1][12]), float(row_num[x-1][13])))

                distancef = numpy.array((float(row_num[x+1][12]), float(row_num[x+1][13])))

                #velocity is defined as distance over time, where time here is frames.
                velocity.append(numpy.linalg.norm((distancef - distancei))/2)

    return velocity
