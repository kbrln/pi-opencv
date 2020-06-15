"""
Image gradient is directional change in intensity or color in an image.
Can be used to find edges in image 

Gradient functions: 
    Laplassian 
    Sobel X
    Sobel Y 
"""

import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("sudoku.png", cv2.IMREAD_GRAYSCALE)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3) #cv_64 is a data type, 64 bit
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelX = np.uint8(np.absolute(sobelX)) # detects chnage in x direction (i.e. vertical lines)

sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY) # combine

titles = ['image', 'laplassian', 'sx', 'sy', 'sobelCombined']
images = [img, lap, sobelX, sobelY, sobelCombined]

for i in range(len(images)):
    plt.subplot(1, len(images), i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()