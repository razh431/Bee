import numpy
import matplotlib.pyplot as plt
import math
import bee1
import csv
import bee_info

def ant_cba_angle_2d(frame):
    bee = bee_info.bee_info(frame)

    #v_cba is vector on cba, v_l is 2 points on left antenna, v_r is angle on right antenna
    y_b, y_s = bee.cba()

    v_cba = [bee.x_base - bee.x_sting, y_b - y_s]
    v_l = [bee.x_left_ant - bee.x_base, bee.y_left_ant - y_b]


    v_r = [bee.x_right_ant - bee.x_base, bee.y_right_ant - y_b]

    left_angle = angle_between(v_cba, v_l)
    right_angle = angle_between(v_cba, v_r)

    # print("left ant angle: " + str(left_angle))
    # print("right ant angle: " + str(right_angle))

    return left_angle, right_angle



def angle_3d(frame):
    bee = bee_info.bee_info(frame)

    max_ant = 52.0
    v_video = [bee.x_left_ant - bee.x_base, bee.y_left_ant - bee.y_base]
    dist = numpy.linalg.norm(v_video)
    angle = math.degrees(numpy.arccos(numpy.clip(dist/52.0, -1.0, 1.0)))

    print(angle)


def ant_len():
    '''returns the 98th precentile of the antennae lengths: let's go with 52'''
    antr_length = []
    antl_length = []

    with open("bee3_antenna.csv") as csvfile:
        reader = csv.reader(csvfile)

        row_num =[row for idx, row in enumerate(reader) if idx in range(22,913)]

        for x in range(0, len(row_num)):
            v_right_ant = numpy.array((float(row_num[x][4]), float(row_num[x][5])))
            v_left_ant = numpy.array((float(row_num[x][1]), float(row_num[x][2])))
            v_base = numpy.array((float(row_num[x][7]), float(row_num[x][8])))

            distr = numpy.linalg.norm(v_right_ant-v_base)
            distl = numpy.linalg.norm(v_left_ant-v_base)

            antr_length.append(distr)
            antl_length.append(distl)
            # if len(antr_length) > 30:
            #     antr_length.remove(min(antr_length))
            #
            # if len(antl_length) > 30:
            #     antl_length.remove(min(antl_length))

    print(numpy.percentile(antr_length, 98))
    print(numpy.percentile(antl_length, 98))

    # antr_length.sort()
    # antl_length.sort()
    # print(antr_length)
    # print(antl_length)

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


# ant_cba_angle_2d(1090)
ant_len()
# angle_3d(1047)
