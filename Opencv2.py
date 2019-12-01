import cv2
import numpy as np
cap = cv2.VideoCapture("videooo.mp4")

fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    try:
        _, frame = cap.read()
#####################################
        cv2.imshow('den',frame)
        fgmask = fgbg.apply(frame)

        cv2.imshow('REs',frame)
        cv2.imshow('Maske',fgmask)

####################################
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    except:
        break
cv2.destroyAllWindows()
cap.release()
