import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)   # show events available in cv2 library

def click_event(event, x, y, flags, param):
    # if event == cv2.EVENT_LBUTTONDOWN:  # show XY coordinates on left click
    #     strXY = f"{x}, {y}"
    #     font = cv2.FONT_HERSHEY_SIMPLEX
    #     cv2.putText(img, strXY, (x, y), font, 0.5, (255, 255, 0), 2)
    #     cv2.imshow('image', img)    #img is a global variable

    # if event == cv2.EVENT_RBUTTONDOWN:  # show BGR channels on right click
    #     blue = img[y, x, 0]
    #     green = img[y, x, 1]
    #     red = img[y, x, 2]
    #     strBGR = f"{blue}, {green}, {red}"
    #     font = cv2.FONT_HERSHEY_SIMPLEX
    #     cv2.putText(img, strBGR, (x, y), font, 0.5, (0, 255, 255), 2)
    #     cv2.imshow('image', img)    #img is a global variable

    # if event == cv2.EVENT_LBUTTONDOWN:  # draw line between 2 clicked points
    #     cv2.circle(img, (x,y), 3, (0, 0, 255), -1)
    #     points.append((x,y)) # store a list of the points clicked coordinates 
    #     if len(points) >= 2: # if we have 2 points 
    #         cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
    #     cv2.imshow('image', img)

    if event == cv2.EVENT_LBUTTONDOWN:  # left click to display colour of the clicked pixel in a new window 
        # blue = img[x, y, 0]
        # green = img[x, y, 1]
        # red = img[x, y, 2]    # makes no difference if x, y swapped ??
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img, (x, y), 3, (0,0, 255), -1)
        mycolorImage = np.zeros((512, 512, 3), np.uint8)

        mycolorImage[:] = [blue, green, red]

        cv2.imshow('color', mycolorImage)


img = np.zeros((512, 512, 3), np.uint8) # create black image 
# img = cv2.imread('lena.jpg')
cv2.imshow('image', img)

points = []

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()