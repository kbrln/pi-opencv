import cv2 
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('opencv-logo.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel) # apply kernel on 2d filter (dst = destintation)

"""As in 1d signals, images can also be filtered with various Low or high pass filters. 
LPF removes noises, blurring images. 
HPF helps find edges
"""
blur = cv2.blur(img, (5,5)) # blur or averaging algo
gaus = cv2.GaussianBlur(img, (5,5), 0)# gaussian filter, is using different weight kernel in x and y direction (like bell curve)
# median filter: replace each pixel value with median of its neighboring pixles (great for salt and pepper noise)
median = cv2.medianBlur(img, 5) # kernel size must be odd and not 1 
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75) # kenel size, sigma colour, sigma space , good for noise removal while keeping sharp edges

titles = ['image', '2D Convolution', 'blur', 'gaussian', 'median', 'bilateralFilter']
images = [img, dst, blur, gaus, median, bilateralFilter]

for i in range(len(images)):
    plt.subplot(1, len(images), i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()