import cv2
from matplotlib import pyplot as plt 

img = cv2.imread('lena.jpg', -1)
cv2.imshow('image', img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# matplot lib has built in options in the window
plt.imshow(img) # read in RGB not BGR, need to convert 
plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()