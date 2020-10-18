import cv2
import os
import csv
import numpy as np
import glob
from start_end import startFrame, endFrame, dlt_small_sheet


"""make sure to change the start and end frames in plot and new_mapping files"""

"""creates a single bee from the swarm"""

cap= cv2.VideoCapture('/Users/rachelzhou/summer_research/swarm6.mp4')

#crop 250 frames of y positions, 200 frames of x. get square
def crop():
    
    #set start frame at the bee.csv start frame, not 1 because we need the swarm video
    cap.set(1, startFrame)
    i= startFrame

    while(int(cap.get(cv2.CAP_PROP_POS_FRAMES) < endFrame)):
        ret, frame = cap.read()
        if ret == False:
            break
        
        #current frame number of video
        frame_num = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        
        #use dlt small sheet excel from DLT readings (spreashseet of where the petioles are)
        with open(dlt_small_sheet) as fd:
            reader=csv.reader(fd)
            frame_num_rows=[row for idx, row in enumerate(reader) if idx == frame_num]
        
        #grab x, y-- the x, y positions of these bees' petioles, which indicates bees location
        x = int(float(frame_num_rows[0][0]))
        y = int(float(frame_num_rows[0][1]))



        path = '/Users/rachelzhou/Research/build_opencv/opencv/samples/python/single/flow'
        cv2.imwrite(os.path.join(path , 'bee'+str(i)+'.jpg'), frame[y-250:y+250, x-200:x])
        print(i)
        i+=1

#attach each frame into a large video from the small sheet data created FROM DLT not BEE PATH
def frame_into_vid(dlt_small_sheet):
    image_folder = 'images' + str(dlt_small_sheet)[3]
    video_name = 'bee' + str(dlt_small_sheet)[3] + '.avi'
    
    #WHY DOESNT OS SORT AUTOMATICALLY UPON CRWATELKRJSLK
    img_list = os.listdir(image_folder)
    img_list.sort()
    
    #find the images in that folder-- bascially if theyre a jpg
    images = [img for img in img_list if img.endswith(".jpg")]

    # images = []
    # for img in os.listdir(image_folder):
    #     if img.endswith(".jpg"):
    #         images.append(img)

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    
    #video frame of origional bee vid is 23.39
    video = cv2.VideoWriter(video_name, 0, 23.39, (width,height))
    
    #join the video together
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
        print(image)

    cv2.destroyAllWindows()
    video.release()


crop()
frame_into_vid(dlt_small_sheet)

cap.release()
cv2.destroyAllWindows()
