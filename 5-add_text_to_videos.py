import cv2 
import datetime 


cap = cv2.VideoCapture(1)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)    # get properties, every number has an associated number which can be used instead
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)



while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True: 
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = f"Width: {width} Height: {height}"
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (10, 50), font, 1, (0, 255, 255), 
                            2, cv2.LINE_AA)    #args: font, font face, color, line thickness
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()