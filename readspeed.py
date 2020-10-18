import cv2
import numpy as np
import os
import csv
import pytesseract
from PIL import Image

"""use pytesseract, optical character recognition for recognizing anemometer video reading"""


#sort the os in terms of numerical order??? why is it different orders from creation
image_folder = 'flow'
img_list = os.listdir(image_folder)
img_list.sort()

#already created image file of images from each video frame
images = [img for img in img_list if img.endswith(".jpg")]

with open('flow.csv', 'a') as f_out:
    writer = csv.writer(f_out)

    #for all frames within the video, saved as images each, read optical character
    for image in images:
        print(image)
        im = Image.open('flow/'+ image)
        writer.writerow((str(image)[3:-4], pytesseract.image_to_string(im, config = 'digits')))
