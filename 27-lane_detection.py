"""
Start of project 

1. Create mask to filter all but region of interest
2. Use edge detection to detect lane lines within ROI

3. Treat video as set of images 
"""

import matplotlib.pylab as plt
import cv2
import numpy as np 

def roi(img, vertices):
    mask = np.zeros_like(img)
    # channel_count = img.shape[2]
    # match_mask_color = (255,) * channel_count
    match_mask_color = 255 # don't need color channel for grayscale 
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def draw_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=np.uint8)
    for line in lines: # returns 4 parameters, start point of line and end point of line 
        for x1, y1, x2, y2 in line: 
            cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=3)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img 


# image = cv2.imread('road.jpg')
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
def process(image): 
    height = image.shape[0]
    width = image.shape[1]
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    canny_image = cv2.Canny(gray_image, 100, 120)   # but we need to remove edges arising from ROI mask, so find canny BEFORE mask 
    roi_vertices = [ (0, height), (width/2, 3*height/4), (width, height)]
    cropped_image = roi(canny_image, np.array([roi_vertices], np.int32)) # now we have edge detected ROI 
    lines = cv2.HoughLinesP(cropped_image, 
            rho=2, 
            theta=np.pi/60, 
            threshold=50, 
            lines=np.array([]), 
            minLineLength=40, 
            maxLineGap=100
            ) # returns line vector of all lines detected
    image_with_lines = draw_lines(image, lines)
    return image_with_lines

# capture video frame 
cap = cv2.VideoCapture('test.mp4')

# main loop
while(cap.isOpened()):
    ret, frame = cap.read()
    frame = process(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() 
cv2.destroyAllWindows()
