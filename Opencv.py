import cv2
import numpy as np



img = cv2.imread('indir.jpg')

hsvColor = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# px = grayscaled[0:50,0:50]
# print(px)
# th = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
# retval ,th = cv2.threshold(hsvColor,20,255,cv2.THRESH_BINARY)

dus_red = np.array([30,150,50])
yuk_red = np.array([255,255,180])

maske = cv2.inRange(hsvColor,dus_red,yuk_red)
res = cv2.bitwise_and(img,img,mask=maske)

cv2.imshow('resim',img)
cv2.imshow('hsv',maske)
cv2.imshow('hsv2',res)
cv2.waitKey(0)
cv2.destroyAllWindows()