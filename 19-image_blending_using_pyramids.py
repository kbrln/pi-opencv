"""
image blending or merging of two images, i.e. blending half of one image with half of other

Steps:
1. Load two images
2. Find Gaussian Pyramids for each image 
3. Find laplacian pyramids
4. Join left half of im1 with right half of im2 in each level fo laplacian pyramid
5. reconstrcut original image from the join image pyramid
"""


import cv2
import numpy as np

apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')
print(apple.shape)
print(orange.shape)

apple_orange = np.hstack((apple[:, :256], orange[:, 256:])) # manually merge images, theres still a hard line separating the two - use blending. 

# generate Gaussian pyramids (6 levels)
apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range(6): # choose 6 levels
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

orange_copy = orange.copy()
gp_orange = [orange_copy]
for i in range(6): # choose 6 levels
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# generate Laplassian pyramids 
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5, 0, -1): 
    gaussian_expanded = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], gaussian_expanded)
    lp_apple.append(laplacian)

orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5, 0, -1): 
    gaussian_expanded = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1], gaussian_expanded)
    lp_orange.append(laplacian)


# add left and riht halves at each level 
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n+=1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

# finally reconstruct iamge 
apple_orange_resconstruct = apple_orange_pyramid[0]
for i in range(1, 6): 
    apple_orange_resconstruct = cv2.pyrUp(apple_orange_resconstruct)
    apple_orange_resconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_resconstruct)


cv2.imshow('apple', apple)
cv2.imshow('orange', orange)
cv2.imshow('apple_orange_resconstruct', apple_orange_resconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()