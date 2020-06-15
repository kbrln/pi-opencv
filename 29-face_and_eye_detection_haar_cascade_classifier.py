"""
Using haar cascade classifier (machine learnign algorithm)

A classifier (cascade of boosted classifiers workign with haar-like features) is trained witha  few hundred 
sample views of a particular object (i.e. face, car) called positive examples that are scaled to same 
size (i.e. 20x20) and negative examples - arbitrary images of the same size. 

Use a pretrained classifier on first an image, then a video 
"""

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
cap = cv2.VideoCapture(1)

while cap.isOpened(): 
    _, img = cap.read()
    # img = cv2.imread('test.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, minNeighbors=4) # this will be a vector of rectangles 

    for (x, y, w, h) in faces: 
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 5)

    # display output
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()