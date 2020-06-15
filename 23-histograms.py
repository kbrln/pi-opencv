"""
Histograms plot pixel intensities of an image. 

Count of pixels (y) against intensity (x)

We can use matplotlib or opencv 
"""

import numpy as np 
import cv2 as cv
from matplotlib import pyplot as plt 

img = cv.imread('lena.jpg', 0) # real image
# b, g, r = cv.split(img)


# # Artifical image
# # img = np.zeros((200, 200), np.uint8)
# # cv.rectangle(img, (0, 100), (200, 200), (255), -1) # -1 is fill
# # cv.rectangle(img, (0, 50), (100, 100), (127), -1) # -1 is fill


# cv.imshow('img', img)
# cv.imshow('b', b)
# cv.imshow('g', g)
# cv.imshow('r', r)

# # plt.hist(img.ravel(), 256, [0, 256])
# plt.hist(b.ravel(), 256, [0, 256])
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])

# OPEN CV METHOD
hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()