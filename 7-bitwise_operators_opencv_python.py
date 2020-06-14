import cv2 
import numpy as np

# create two images 
img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = np.zeros((250, 500, 3), np.uint8)
img2[:, 250:500, :] = 255


# bitAnd = cv2.bitwise_and(img2, img1) # bit and, (segmented into 0 and non-zero, 1-255 counts as 1)
# bitOr = cv2.bitwise_or(img2, img1)
# bitXor = cv2.bitwise_xor(img2, img1)
bitNot1 = cv2.bitwise_not(img1)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("bitAnd", bitNot1)

cv2.waitKey(0)
cv2.destroyAllWindows()
