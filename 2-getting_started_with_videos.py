import cv2

cap = cv2.VideoCapture(1)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480)) # create output handle

while(cap.isOpened()): # check whether capture is valid file/stream
    ret, frame = cap.read() # returns true/false in ret whether frame is available or not, and frame in frame
    if ret==True:   # if frame is returned successfully
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))   # display video properties

        out.write(frame) # write video stream to output handle (file)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert to grayscale 
        cv2.imshow('frame', gray) # show video stream

        if cv2.waitKey(1) & 0xFF == ord('q'):   # if q is pressed, exit loop
            break
    else: 
        break

cap.release()
out.release()
cv2.destroyAllWindows()