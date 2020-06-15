import numpy as np 
import cv2

img = cv2.imread('opencv-logo.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply threshold to get binary image 
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
# contours will be a python list of all contours in image, each being an np array of (x,y) coords
# of boundary points 
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print(str(len(contours)))

cv2.drawContours(img, contours, 1, (0, 255, 0), 3)  #first numeric arg is choose which contour to display, -1 means all

cv2.imshow('Image', img)
cv2.imshow('Image GRAY', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()