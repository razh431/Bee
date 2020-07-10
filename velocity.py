import numpy
import math
import csv
import bee1

"""find velocity of bees"""

def vel():
    '''returns the 98th precentile of the antennae lengths: let's go with 52'''
    v = []

    with open("bee3_antenna.csv") as csvfile:
        reader = csv.reader(csvfile)

        row_num =[row for idx, row in enumerate(reader) if idx in range(21,913)]

        velocity = []
        for x in range(0, len(row_num)):
            petiole = numpy.array((float(row_num[x][19]), float(row_num[x][20])))

            if x > 0:
                distancef = numpy.array((float(row_num[x-1][19]), float(row_num[x-1][20])))

                #velocity is defined as distance over time, where time here is frames.
                velocity.append(numpy.linalg.norm(distancef - petiole))

    return velocity
