import numpy as np

import cv2 

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

# show some image properties
# print(img.shape)
# print(img.size)
# print(img.dtype)
# print(type(img))    # numpy array

# split image into channels and merge back together
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

# copy and past ROI (region of interest) to antoher location in the image
ball = img[280:340, 330:390]    # top left and bottom right corners of the ball in image, indexed in numpy array
img[273:333, 100:160] = ball

#resize images so they are compatible with cv2.add method
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))
# dst = cv2.add(img, img2)    # must be same size, add is like overlay
dst = cv2.addWeighted(img, .5, img2, .1, 0)     # change weight (transparency)

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()