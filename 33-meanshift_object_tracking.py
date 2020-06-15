import numpy as np 
import cv2 as cv
cap = cv.VideoCapture('slow_traffic_small.mp4')

"""
Disadvantage of meanshift 
- is u need to provide INITIAL location of window/roi
- Size of window does not change (no depth adjustment as objects get bigger as they get closer. )

Steps: 
1. take first frame of video
2. setup initial location of window
3. set up the roi for tracking
4. setup termination critiera, either 10 iteration or move by at least 1 pt (histogram back projection)
"""

# first frame 
ret, frame = cap.read()

# intiial location of window 
x, y, width, height = 300, 200, 100, 50 # hardcoded 
track_window = (x, y, width, height)

#set up roi for tracking
roi = frame[y:y+height, x:x+width]

#define histogram back projection image
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0.,60., 32.)), (np.array((180., 255., 255)))) # avoid low light values
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

# setup termination critieria, either 10 iteration or move by at least 1 pt 
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10 ,  1)

cv.imshow('roi', roi)

while(1): 
    ret, frame = cap.read()
    if ret == True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1) # [0] means hue channel only, this is the back projectio imag
        # apply MEANSHIFT to get new location
        ret, track_window = cv.meanShift(dst, track_window, term_crit)

        # Draw it on image
        x, y, w, h = track_window
        final_image = cv.rectangle(frame, (x, y), (x+w, y+h), 255, 3)
        
        cv.imshow('dst', dst)
        cv.imshow('final_image', final_image)
        k = cv.waitKey(30) & 0xff
        if k ==  27: 
            break

    else: 
        break