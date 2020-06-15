"""
Pyramid representation is a type of multi-scale signal represeneation in which
a signal or an image is subject to repeated smoothing and subsampling 
(imagine pyramid where the image is the horizontal cross section, getting smaller as it rises)

Use: helps blend and reconstruct images 

Types: 
1. Gaussian
2. Laplassian : 
    a level in laplacian pyramid is formed by the difference between that level in 
    gaussian pyramid and expanded version of its upper level in gaussian pyramid
"""

import cv2 
import numpy as np
img = cv2.imread('lena.jpg')

# Gaussian pyramids
# lr1 = cv2.pyrDown(img)   # reduce resolution of image
# lr2 = cv2.pyrDown(lr1)  # further reduce resoltuion
# hr1 = cv2.pyrUp(lr2) # increase resolution, loses information 

cv2.imshow('Original', img)
# cv2.imshow('pyrdown 1', lr1)
# cv2.imshow('pyrdown 2', lr2)
# cv2.imshow('pyrup 1', hr1)

layer = img.copy()
gp = [layer]

for i in range(6): # to create 5 pyramid layers
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i), layer)


# Laplassian pyramid
layer = gp[5]
cv2.imshow('upper level Gaussian Pyramid', layer)
lp = [layer]    # create list of laplassian pyramids

for i in range(5, 0, -1): 
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()