import bee1
import numpy as np
import matplotlib.pyplot as plt
import math
import csv
import cv2
import bee_info
from start_end import startFrame, endFrame, path

""" most important file for visualization. Maps the trained data set of each body feature into the large swarm video"""


#get position of bee from the singular video and adjust (remap them accordingly) onto the larger swarm video. 
def pos(bee, frame_num, body_part_x, body_part_y):
    bee_info.bee_update_info(bee, frame_num)

    x, y = adjust_pos(body_part_x, body_part_y, bee, frame_num)

    return x, y

#returns adjusted position by calculating its position relative to petiole. petiole is at center of bee
def adjust_pos(body_part_x, body_part_y, bee, frame_num):

    #petiole is at 100,100 around, a few pixels off. 
    with open(path) as fd:
        reader=csv.reader(fd)
        #the 2d array of x and y indices of the needed frame
        frame_num_rows=[row for idx, row in enumerate(reader) if idx == frame_num]
    
    #get each x, y from the array
    x = int(float(frame_num_rows[0][0]))
    y = int(float(frame_num_rows[0][1]))

    #dumb way to do this but i did it: if even, then it's x position

    # print("frame_num right before adjusted: " + str(frame_num))
    # print("base x: " + str(body_part_x))
    # print("base y: " + str(body_part_y))
    
    #adjust body part according to the position relative to petiole
    if body_part_x > 100:
        x += body_part_x - 100
    elif body_part_x < 100:
        x -= 100 - body_part_x

    if body_part_y > 100:
        y += body_part_y - 100
    elif body_part_y < 100:
        y -= 100 - body_part_y

    return x, y

def map():
    cap= cv2.VideoCapture('/Users/rachelzhou/summer_research/swarm6.mp4')


    cap.set(1, startFrame)

    bee = bee_info.bee_info(0)

    while(int(cap.get(cv2.CAP_PROP_POS_FRAMES)) < endFrame):
        ret, frame = cap.read()
        if ret == False:
            break

        frame = cv2.resize(frame,(int(frame.shape[1]/4),int(frame.shape[0]/4)))

        print(int(cap.get(cv2.CAP_PROP_POS_FRAMES)))
        
        body_parts = [
            bee.x_base,
            bee.y_base,
            bee.x_sting,
            bee.y_sting,
            bee.x_right_ant,
            bee.y_right_ant,
            bee.x_left_ant,
            bee.y_left_ant
        ]

        #for each body part, update the body parts positions and map it out
        for i in range(0, len(body_parts), 2):
            x, y = pos(bee, int(cap.get(cv2.CAP_PROP_POS_FRAMES)-startFrame), body_parts[i], body_parts[i+1])

            # print("frame_num right before adjusted: " + str(frame_num))
            # print("base x: " + str(x))
            # print("base y: " + str(x))

            x = np.float32(x/4)
            y = np.float32(y/4)

            #opencv is BGR instad of RGB
            #different bgrs according to what body part. hard coded. 
            if (i == 0):
                BGR = (198, 173, 0)
            elif (i == 2):
                BGR = (54, 115, 230)
            elif (i == 3):
                BGR = (227, 99, 55)
            else:
                BGR = (147, 58, 52)
            circle = cv2.circle(frame, (x, y), 3, BGR, -1)
        cv2.imshow('frame', frame)

        cv2.waitKey(1500)


    cv2.destroyAllWindows()
    video.release()


#starts bee from 17 row in csv
map()
