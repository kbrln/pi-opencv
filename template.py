import cv2 
import numpy as np
from matplotlib import pyplot as plt



img = cv2.imread("messi5.jpg", 0)


titles = ['image']
images = [img]

for i in range(len(images)):
    plt.subplot(1, len(images), i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()