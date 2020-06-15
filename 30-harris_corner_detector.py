"""
Harris corner detector

1. determine which windows produce very large variations in intensity when moved in both x and y directions
2. with each such window found , a score R is comptued
3. after applying a threshold to this score, important corners are selected and marked. 
"""

import numpy as np
import cv2 as cv

img = cv.imread('chessboard.png')
img = cv.pyrDown(cv.pyrDown(img))

cv.imshow('img', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv.cornerHarris(gray, 2, 3, 0.04)

dst = cv.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv.imshow('dst', img)

if cv.waitKey(0) & 0xff == 27: 
    cv.destroyAllWindows()