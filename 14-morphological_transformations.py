"""
Getting rid of noise after thresholding 
"""

import cv2 
import numpy as np 
from matplotlib import pyplot as plt


img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((5,5), np.uint8) # kernel is a shape to apply on the image, i.e 2x2
dilation = cv2.dilate(mask, kernel, iterations=2) # last arg is iterations
erosion = cv2.erode(mask, kernel, iterations=2)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)        # erosion then dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)       # dilation then erosion

# other operators 
# morphological gradient = difference between dilation and erosion 
# top hat 
titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing']
images = [img, mask, dilation, erosion, opening, closing]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()