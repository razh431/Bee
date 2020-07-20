import csv
import os
import numpy as np


"""create csv with swarm x_y and then xy positions of everything else

x positions:
E	Left antennae [][4]
G	Right antennae [6]
I	Base [8]
K	Sting [10]
M	Petiole [12]

y is jsut 1 letter off

have to edit the output csv file because I can't figure out how to move everything :
"""

#video start frame from swarm
#1: 1002-2352
#2: 1550- 2310
#3: 1029- 1900
#4: 1356-1856
#6: 1920 - 2815
startFrame = 1920
endFrame = 2815

path = 'bee6.csv'
#
#csv from big data sheet with all the xsv
#csv_row is the starting row with prediction that is close to 1
csv_row = 0
video_num = 2
dlt_small_sheet = "air_speedxypts.csv"
dlt_big_sheet = "bee6DLC_resnet50_bee_walkingJun4shuffle1_311000.csv"

cols = [1, 2, 4, 5, 7, 8, 16, 17, 19, 20]

def xy():
    with open(dlt_small_sheet) as f,open(str(dlt_big_sheet)[:4] + '.csv', 'a') as f_out:
         reader = csv.reader(f)
         writer = csv.writer(f_out)
         for num, row in enumerate(reader):
             # print(row)
             if num >= startFrame and num <= endFrame:
                 writer.writerow((row[0], row[1]))

    return num

def rest(num1):
    with open(dlt_big_sheet) as f, open(str(dlt_big_sheet)[:4] + '.csv', 'a') as f_out:
         reader = csv.reader(f)
         writer = csv.writer(f_out)
         for num, row in enumerate(reader):
             if num >= 3 and num <= num1 + 1:
                 writer.writerow(("", row[0], row[1], row[2], row[4], row[5], row[7], row[8], row[16], row[17], row[19], row[20]))

def main():
    num = xy()
    rest(num)

if __name__ == '__main__':
    main()
