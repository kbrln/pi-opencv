"""
Technique for generating foreground mask, therefore capturing foreground subject information wrt static 
background . 
"""

import numpy as np
import cv2 as cv
cap = cv.VideoCapture('vtest.avi')
# kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3)) # needed for GMG

fgbg = cv.bgsegm.createBackgroundSubtractorMOG() # foreground background 
# fgbg = cv.createBackgroundSubtractorMOG2(detectShadows=False) # another method
# fgbg = cv.bgsegm.createBackgroundSubtractorGMG()
# fgbg = cv.createBackgroundSubtractorKNN(detectShadows=False) # 

while True: 
    ret, frame = cap.read()
    if frame is None: 
        break

    fgmask = fgbg.apply(frame)
    #fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel) # this is required for GMG method, otherwise nothing shows

    cv.imshow('Frame', frame)
    cv.imshow('FG MASK Frame', fgmask)


    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

cap.release()
cv.destroyAllWindows()