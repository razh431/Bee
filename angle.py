import numpy
import matplotlib.pyplot as plt
import math
import bee1
import csv
import bee_info
from start_end import startFrame, endFrame, path


"""these frames are adjusted from new excel spreadsheet"""

def ant_cba_angle_2d(frame):
    # print(frame)
    bee = bee_info.bee_info(frame)
    
    #central body access from bee, 2 points from cba
    y_b, y_s = bee.cba()
    
    #calculatng cba, left antenna line, right antenna as a straight line
    v_cba = [bee.x_base - bee.x_sting, y_b - y_s]
    v_l = [bee.x_left_ant - bee.x_base, bee.y_left_ant - y_b]
    v_r = [bee.x_right_ant - bee.x_base, bee.y_right_ant - y_b]

    left_angle = angle_between(v_cba, v_l)
    right_angle = angle_between(v_cba, v_r)

    # print("left ant angle: " + str(left_angle))
    # print("right ant angle: " + str(right_angle))

    return left_angle, right_angle


def angle_3d(frame):
    #find 3d angle of bee, not used
    bee = bee_info.bee_info(frame)

    max_ant = 52.0
    v_video = [bee.x_left_ant - bee.x_base, bee.y_left_ant - bee.y_base]
    dist = numpy.linalg.norm(v_video)
    angle = math.degrees(numpy.arccos(numpy.clip(dist/52.0, -1.0, 1.0)))


    #rate of change of angle-- only positive values right now
def roc_angle(total_angle):

    change = []
    for x, ang in enumerate(total_angle):
        if x > 0 and x < len(total_angle) - 1:
            change.append((total_angle[x-1] - total_angle[x+1])/2)

    return change


#calculates antennae length 
def ant_len(startFrame, endFrame):
    '''returns the 95th precentile of the antennae lengths'''
    antr_length = []
    antl_length = []

    with open(path) as csvfile:
        reader = csv.reader(csvfile)

        row_num =[row for idx, row in enumerate(reader) if idx in range(startFrame, endFrame)]
    
        #calculate antennae lengths from pythagorean theorum of left, right, base attributes
        #numbers correspond to excel shets from the bee.csv files from path
        for x in range(0, len(row_num)):
            v_right_ant = numpy.array((float(row_num[x][6]), float(row_num[x][7])))
            v_left_ant = numpy.array((float(row_num[x][4]), float(row_num[x][5])))
            v_base = numpy.array((float(row_num[x][8]), float(row_num[x][9])))

            distr = numpy.linalg.norm(v_right_ant-v_base)
            distl = numpy.linalg.norm(v_left_ant-v_base)

            antr_length.append(distr)
            antl_length.append(distl)

    #grabs percentiles
    print(numpy.percentile(antr_length, 95))
    print(numpy.percentile(antl_length, 95))



    return antl_length, antr_length

def unit_vector(vector):
    """ Returns the unit vector of the vector."""
    assert(vector != [0,0])
    return vector / numpy.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in degrees between vectors 'v1' and 'v2' """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)

    #takes out if vectors are 1 or -1 (basically if they're the same direction)
    angle = math.degrees(numpy.arccos(numpy.clip(numpy.dot(v1_u, v2_u), -1.0, 1.0)))
    return angle
