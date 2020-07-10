import cv2
import os
import csv
import numpy as np
import glob

cap= cv2.VideoCapture('/Users/rachelzhou/summer_research/swarm6.mp4')
def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

def crop():

    startFrame = 1029
    cap.set(1, startFrame)
    i= startFrame

    while(int(cap.get(cv2.CAP_PROP_POS_FRAMES) < 1940)):
        ret, frame = cap.read()
        if ret == False:
            break

        frame_num = int(cap.get(cv2.CAP_PROP_POS_FRAMES))

        with open('single_bee_vids/bee3_1029_1940xypts.csv') as fd:
            reader=csv.reader(fd)
            frame_num_rows=[row for idx, row in enumerate(reader) if idx == frame_num]

        x = int(float(frame_num_rows[0][0]))
        y = int(float(frame_num_rows[0][1]))

        path = '/Users/rachelzhou/Research/build_opencv/opencv/samples/python/single/images1'
        cv2.imwrite(os.path.join(path , 'bee'+str(i)+'.jpg'), frame[y-100:y+100, x-100:x+100])
        print(i)
        i+=1

def frame_into_vid():
    image_folder = 'images1'
    video_name = 'bee3.avi'

    img_list = os.listdir(image_folder)
    img_list.sort()

    images = [img for img in img_list if img.endswith(".jpg")]

    # images = []
    # for img in os.listdir(image_folder):
    #     if img.endswith(".jpg"):
    #         images.append(img)

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 23.39, (width,height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
        print(image)

    cv2.destroyAllWindows()
    video.release()


# make_480p()
# crop()
frame_into_vid()

cap.release()
cv2.destroyAllWindows()
