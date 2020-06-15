"""
Canny edge detector is an edge detection operator 
that  uses multi-stage algorithm to detect wide
range of edges in images

Algorithm: 
1. Reduce noise
2. Calculate gradient
3. Non-max suppression
4. Double threshold
5. Edge tracking by hysteresis
"""


import cv2 
import numpy as np
from matplotlib import pyplot as plt



img = cv2.imread("messi5.jpg", 0)
canny = cv2.Canny(img, 100, 200) # img, threshold1, threshold2, 

titles = ['image', 'canny']
images = [img, canny]

for i in range(len(images)):
    plt.subplot(1, len(images), i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()