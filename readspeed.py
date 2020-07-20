import cv2
import numpy as np
import os
import csv
import pytesseract
from PIL import Image


image_folder = 'flow'
img_list = os.listdir(image_folder)
img_list.sort()

images = [img for img in img_list if img.endswith(".jpg")]

with open('flow.csv', 'a') as f_out:
    writer = csv.writer(f_out)

    for image in images:
        print(image)
        im = Image.open('flow/'+ image)
        writer.writerow((str(image)[3:-4], pytesseract.image_to_string(im, config = 'digits')))
