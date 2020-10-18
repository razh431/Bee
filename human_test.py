import cv2
import numpy as np

"""use opencv to get specific locations of bee positions to verify how accurate the model predictions are"""

#draw circle when mouse events click
def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x,y)]
        print(refPt)
        
path = 'images2/bee2200.jpg'
img = cv2.imread(path)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

#if mouseclick, print mouse x y positions
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        print(mouseX,mouse)
