import bee1
import numpy as np
import matplotlib.pyplot as plt
import math
import csv
import cv2
import antennae

def pos(bee, frame_num):
    antennae.bee_update_info(bee, frame_num)

    body_parts = [
        bee.x_base,
        bee.y_base,
        # bee.x_sting,
        # bee.y_sting,
        # bee.x_right_ant,
        # bee.y_right_ant,
        # bee.x_left_ant,
        # bee.y_left_ant
    ]
    for i in range(0, len(body_parts), 2):
        x, y = adjust_pos(body_parts[i], body_parts[i+1], bee, frame_num)
    return x, y

def adjust_pos(body_part_x, body_part_y, bee, frame_num):

    #petiole is at 100,100 around, a few pixels off
    with open('single_bee_vids/bee3_1029_1940xypts.csv') as fd:
        reader=csv.reader(fd)
        frame_num_rows=[row for idx, row in enumerate(reader) if idx == frame_num]

    x = int(float(frame_num_rows[0][0]))
    y = int(float(frame_num_rows[0][1]))

    #dumb way to do this: if even, then it's x position

    # print("frame_num right before adjusted: " + str(frame_num))
    # print("base x: " + str(bee.x_base))
    # print("base y: " + str(bee.y_base))
    if body_part_x > 100:
        x += body_part_x - 100
    elif body_part_x < 100:
        x -= body_part_x - 100

    if body_part_y > 100:
        y += body_part_y - 100
    elif body_part_y < 100:
        y -= body_part_y - 100

    return x, y

def map():
    cap= cv2.VideoCapture('/Users/rachelzhou/summer_research/swarm6.mp4')

    #really really weird calculation: 1029-- 0-- 4, so 17th frame from excel
    # that I was using becomes 1047- 17th
    startFrame = 1047
    cap.set(1, startFrame)

    bee = antennae.bee_info(startFrame)

    while(int(cap.get(cv2.CAP_PROP_POS_FRAMES)) < 1100):
        ret, frame = cap.read()
        if ret == False:
            break

        frame = cv2.resize(frame,(int(frame.shape[1]/4),int(frame.shape[0]/4)))

        print(int(cap.get(cv2.CAP_PROP_POS_FRAMES)))

        x, y = pos(bee, int(cap.get(cv2.CAP_PROP_POS_FRAMES)))
        x = np.float32(x/4)
        y = np.float32(y/4)

        #opencv is BGR instad of RGB
        circle = cv2.circle(frame, (x, y), 3, (198, 173, 0), -1)
        cv2.imshow('frame', frame)

        cv2.waitKey(1500)


    cv2.destroyAllWindows()
    video.release()


#starts bee from 17 row in csv
map()
