import numpy as np
import matplotlib.pyplot as plt
import math
import csv
import bee1
from start_end import startFrame, endFrame, path

def bee_info(frame_num):

    with open(path) as csvfile:
        reader = csv.reader(csvfile) # change contents to floats
        #20th frame for now, 1st 3 is just headers

        #1027 is magic number: start of frames in csv don't edit if playing around with code
        row_num =[row for idx, row in enumerate(reader) if idx == frame_num]

    x_left_ant = float(row_num[0][4])
    y_left_ant = float(row_num[0][5])
    x_right_ant = float(row_num[0][6])
    y_right_ant = float(row_num[0][7])
    x_base = float(row_num[0][8]) #150.921
    y_base = float(row_num[0][9]) #109.225
    x_sting = float(row_num[0][10]) #31.59
    y_sting = float(row_num[0][11]) #43.599
    x_petiole = float(row_num[0][12]) #102.3979
    y_petiole = float(row_num[0][13]) #85.9267

    bee = bee1.Bee(x_base, y_base, x_sting, y_sting, x_petiole, y_petiole, x_right_ant, y_right_ant, x_left_ant, y_left_ant)

    return bee

def bee_update_info(bee, frame_num):
    with open(path) as csvfile:
        reader = csv.reader(csvfile) # change contents to floats
        #20th frame for now, 1st 3 is just headers
        row_num =[row for idx, row in enumerate(reader) if idx == frame_num]

    bee.x_base = float(row_num[0][8]) #150.921
    bee.y_base = float(row_num[0][9]) #109.225
    bee.x_sting = float(row_num[0][10]) #31.59
    bee.y_sting = float(row_num[0][11]) #43.599
    bee.x_petiole = float(row_num[0][12]) #102.3979
    bee.y_petiole = float(row_num[0][13]) #85.9267

    bee.x_right_ant = float(row_num[0][6])
    bee.y_right_ant = float(row_num[0][7])
    bee.x_left_ant = float(row_num[0][4])
    bee.y_left_ant = float(row_num[0][5])
