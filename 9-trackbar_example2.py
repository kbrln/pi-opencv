import numpy as np
import cv2 as cv

def nothing(x):
    print(x)

cv.namedWindow('image')

cv.createTrackbar('CP', 'image', 50, 400, nothing) # pass in trackbar name and window name, min value, max value and callback

switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    img = cv.imread('lena.jpg') # read coloured image
    
    pos = cv.getTrackbarPos('CP', 'image')

    font = cv.FONT_HERSHEY_COMPLEX
    cv.putText(img, str(pos), (50, 150), font, 4, (0, 0, 255))

    k = cv.waitKey(1) & 0xFF
    if k == 27: # esc key
        break

    s = cv.getTrackbarPos(switch, 'image')
    
    if s==0: 
        pass
    else: 
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    img = cv.imshow('image', img)   # assign image to itself 
cv.destroyAllWindows()