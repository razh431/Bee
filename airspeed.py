import numpy
import csv
import math
from start_end import startFrame, endFrame, path

"""grabs air speed from airflow data (from the video) put into list""" 

def airv():
    with open('flow.csv') as csvfile:
        reader = csv.reader(csvfile)
        airspeed = []
        row_num = [row for idx, row in enumerate(reader)]
        # print(row_num[1][0])

        for x in row_num[startFrame:endFrame]:
            airspeed.append(x[1])

    print(len(airspeed))
    return airspeed
