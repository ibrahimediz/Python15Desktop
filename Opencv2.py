import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while(1):
    try:
        _, frame = cap.read()
#####################################
        

####################################
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    except:
        break
cv2.destroyAllWindows()
cap.release()
