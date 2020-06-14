import cv2 

img = cv2.imread('lena.jpg', -1)
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF # captures key value , recommended to use mask if running 64bit

if k==27: # if Esc is pressed, close image without saving
    cv2.destroyAllWindows()
elif k == ord('s'): # if s is pressed, close and save image
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()